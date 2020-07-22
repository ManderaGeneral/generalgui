"""Spreadsheet class that inherits Page"""

from generalgui import Page, Label, Frame, Grid

from generalvector import Vec2

import pandas as pd

from tkinter import filedialog
from generalfile import File

from generallibrary.functions import changeArgsAndKwargs, getParameter
from generallibrary.types import typeChecker

# import statistics

import numpy as np


def ascending(attrName):
    """
    Generate a decorator based on attrName that works both for row and coloumn

    :param str attrName: Should be "previousColumnSort" or "previousRowSort"
    """
    def wrapper(func):
        """Decorator to automatically make the ascending parameter toggleable"""
        def decorator(self, *args, **kwargs):
            """."""
            cellValue = getParameter(func, args, kwargs, "cellValue")

            if getParameter(func, args, kwargs, "ascending") is None:
                ascending = True
                if getattr(self, attrName) == cellValue:
                    ascending = False
                    setattr(self, attrName, None)
                else:
                    setattr(self, attrName, cellValue)

                changeArgsAndKwargs(func, args, kwargs, ascending=ascending)

            return func(self, *args, **kwargs)
        return decorator
    return wrapper


def loadDataFrame(func):
    """Decorator to automatically reload dataframe once it's been changed"""
    def f(self, *args, **kwargs):
        """."""
        result = func(self, *args, **kwargs)
        self.loadDataFrame()
        return result
    return f

def indexValue(func):
    """Decorator to change the cellValue parameter to one index"""
    def f(self, *args, **kwargs):
        """."""
        return _cellValue(func, self, args, kwargs, index=True)
    return f

def headerValue(func):
    """Decorator to change the cellValue parameter to one header"""
    def f(self, *args, **kwargs):
        """."""
        return _cellValue(func, self, args, kwargs, header=True)
    return f

def _cellValue(func, self, args, kwargs, index=False, header=False):
    """Helper for indexValue and headerValue decorators"""
    cellValue = getParameter(func, args, kwargs, "cellValue")

    element = None
    if cellValue is None:
        if self.app.menuTargetElement is None:
            raise ValueError("cellValue is None and app.menuTargetElement is None")

        element = self.app.menuTargetElement
        if not typeChecker(element, ("Button", "Label"), error=False):  # Because element can be Frame
            return

    elif typeChecker(cellValue, "Event", error=False):
        event = cellValue
        element = event.widget.element

    if element is not None:
        grid = element.parentPage
        spreadsheet = grid.getFirstParentByClass("Spreadsheet")
        if grid == spreadsheet.mainGrid:
            gridPos = grid.getGridPos(element)
            if index:
                value = spreadsheet.dataFrame.index[gridPos.y - 1]
            elif header:
                value = spreadsheet.dataFrame.columns[gridPos.x]
            else:
                raise ValueError("index or header has to be True")
        else:
            value = element.getValue()
        args, kwargs = changeArgsAndKwargs(func, args, kwargs, cellValue=value)

    return func(self, *args, **kwargs)


class Spreadsheet(Page):
    """
    Controls multiple grids in a certain way to make it all look cohesive.
    Has optional scrollbars and optional fixed row / column for keys.
    Built-in right-clickable menu, if keys are disabled then those menu options can be accessed by right-clicking main grid instead.

    Keywords:
        Keys -> Header / Index

        Header (df.columns) -> Column keys

        Index (df.index) -> Row keys

    Fillerframes for mainGrid:
     *      xhhhh
     *      xmmmm

     * xx   xhhhh
     * im   immmm
     * im   immmm
     * im   immmm

    i=indexFrame, h=headerFrame, m=mainCell, x=empty, f=frame
    """
    def __init__(self, parentPage=None, width=300, height=300, cellHSB=False, cellVSB=False, columnKeys=True, rowKeys=True, hideMultiline=True, **parameters):
        super().__init__(parentPage=parentPage, width=width, height=height, relief="solid", borderwidth=1, resizeable=True, **parameters)

        # Menus to put in respective keys grid if they exist, otherwise it's put in main grid
        menus = {
            "Row": {
                "Index:": self.getIndexName,
                "Row:": self.getRowName,
                "Average:": self.getRowAverage,

                "Sort_row": self.sortRow,
                "Sort_index": self.sortIndex,

                "Remove_row": self.dropRow,

                "Make_row_header": self.makeRowHeader,
                "Reset_index": self.resetIndex,
            },
            "Column": {
                "Header:": self.getHeaderName,
                "Column:": self.getColumnName,
                "Average:": self.getColumnAverage,

                "Sort_column": self.sortColumn,
                "Sort_header": self.sortHeader,

                "Remove_column": self.dropColumn,

                "Make_column_index": self.makeColumnIndex,
                "Reset_header": self.resetHeader,
            }
        }

        self.cellHSB = cellHSB
        self.cellVSB = cellVSB
        self.columnKeys = columnKeys
        self.rowKeys = rowKeys
        self.previousColumnSort = None
        self.previousRowSort = None
        self.dataFrameIsLoading = False

        if self.columnKeys:
            self.columnKeysPageContainer = Page(self, pack=True, fill="x", padx=1 if self.rowKeys else 0)

            if self.rowKeys:
                self.columnKeysFillerLeft = Frame(self.columnKeysPageContainer, side="left", fill="y")

            self.headerGrid = Grid(self.columnKeysPageContainer, height=30, pack=True, side="left", scrollable=True, mouseScroll=False, fill="x", expand=True)
            self.headerGrid.menu("Column", **menus["Column"])

        if self.rowKeys:
            self.rowKeysPageContainer = Page(self, pack=True, width=0, side="left", fill="y", pady=1 if self.columnKeys else 0)
            self.indexGrid = Grid(self.rowKeysPageContainer, pack=True, side="top", width=100, scrollable=True, mouseScroll=False, fill="both", expand=True)
            self.indexGrid.menu("Row", **menus["Row"])

        self.mainGrid = Grid(self, scrollable=True, hideMultiline=hideMultiline, hsb=cellHSB, vsb=cellVSB, pack=True, fill="both", expand=True)

        if self.columnKeys:
            if cellVSB:
                Frame(self.columnKeysPageContainer, side="left", width=21, fill="y")  # To fill out for existing VSB in mainGrid

        if self.rowKeys:
            if cellHSB:
                Frame(self.rowKeysPageContainer, side="top", height=20, fill="x")  # To fill out for existing HSB in mainGrid. Height -1 for pady=1 in container.

        # Update headers whenever canvas moves (Manual scrollbar, mousewheel and right-click drag)
        if self.rowKeys or self.columnKeys:
            self.mainGrid.canvasFrame.createBind("<Configure>", lambda event: self._syncKeysScroll(event), add=True)

        if not self.rowKeys:
            self.mainGrid.menu("Row", **menus["Row"])

        if not self.columnKeys:
            self.mainGrid.menu("Column", **menus["Column"])

        self.dataFrame = pd.DataFrame()

        self.pack()

        self.menu("Spreadsheet",
                  Save_as_tsv=self.saveAsTSV,
                  Load_tsv_file=self.loadTSV,
                  Clear_all=self.clearAll,
                  )

        if hideMultiline:
            self.menu("Spreadsheet", add=True,
                      Show_multilines=lambda: self.toggleAllMultilines(True),
                      Hide_multilines=lambda: self.toggleAllMultilines(False),
                      )


    defaultHeaderName = "headers"
    defaultIndexName = "indexes"

    @indexValue
    def getRowAverage(self, cellValue=None):
        """Return the row average"""
        try:
            return np.average(self.dataFrame.loc[[cellValue]].values[0])
        except (TypeError, AttributeError):
            pass

    @headerValue
    def getColumnAverage(self, cellValue=None):
        """Return the column average"""
        try:
            return np.average(self.dataFrame[cellValue].values)
        except TypeError:
            return None

    @indexValue
    def getRowName(self, cellValue=None):
        """Return the row name"""
        return cellValue

    @headerValue
    def getColumnName(self, cellValue=None):
        """Return the column name"""
        return cellValue

    def getHeaderName(self):
        """Return the header name"""
        return self.dataFrame.columns.name

    def getIndexName(self):
        """Return the index name"""
        return self.dataFrame.index.name

    @loadDataFrame
    @ascending("previousRowSort")
    def sortHeader(self, cellValue=defaultHeaderName, ascending=None):
        """
        Sort headers in dataframe
        self.preivousRowSort is assigned to cellValue to keep track of ascending toggling
        """
        try:
            self.dataFrame.sort_index(inplace=True, axis=1, ascending=ascending)
        except TypeError:
            pass

    @loadDataFrame
    @ascending("previousColumnSort")
    def sortIndex(self, cellValue=defaultIndexName, ascending=None):
        """
        Sort index in dataframe
        self.previousColumnSort is assigned to cellValue to keep track of ascending toggling
        """
        try:
            self.dataFrame.sort_index(inplace=True, axis=0, ascending=ascending)
        except TypeError:
            pass

    @indexValue
    @loadDataFrame
    @ascending("previousRowSort")
    def sortRow(self, cellValue=None, ascending=None):
        """Sort a row in dataframe"""
        try:  # In case of mixed values
            self.dataFrame.sort_values(inplace=True, axis=1, by=[cellValue], ascending=ascending)
        except TypeError:
            return

    @headerValue
    @loadDataFrame
    @ascending("previousColumnSort")
    def sortColumn(self, cellValue=None, ascending=None):
        """Sort a column in dataframe"""
        try:  # In case of mixed values
            self.dataFrame.sort_values(inplace=True, axis=0, by=[cellValue], ascending=ascending)
        except TypeError:
            return

    @loadDataFrame
    @indexValue
    def dropRow(self, cellValue=None):
        """Drop a row in dataframe"""
        if self.dataFrame.shape[0] == 1:
            self.clearAll()
        else:
            self.dataFrame.drop(cellValue, axis="rows", inplace=True)

    @loadDataFrame
    @headerValue
    def dropColumn(self, cellValue=None):
        """Drop a column in dataframe"""
        if self.dataFrame.shape[1] == 1:
            self.clearAll()
        else:
            self.dataFrame.drop(cellValue, axis="columns", inplace=True)

    @loadDataFrame
    @indexValue
    def makeRowHeader(self, cellValue=None):
        """Turn a row to header and make current header a row in dataframe"""
        self.moveHeaderToRow()
        row = self.dataFrame.loc[[cellValue]].values[0]
        self.dataFrame.columns = row
        if cellValue == self.defaultHeaderName:
            self.dataFrame.columns.name = None
        else:
            self.dataFrame.columns.name = cellValue
        self.dropRow(cellValue)

    @loadDataFrame
    @headerValue
    def makeColumnIndex(self, cellValue=None):
        """Turn a column to index and make current index a column in dataframe"""
        self.moveIndexToColumn()

        column = self.dataFrame[cellValue].values
        self.dataFrame.index = column

        if cellValue == self.defaultIndexName:
            self.dataFrame.index.name = None
        else:
            self.dataFrame.index.name = cellValue

        self.dropColumn(cellValue)

    @loadDataFrame
    def resetHeader(self):
        """Reset header to integers"""
        self.moveHeaderToRow()
        self.dataFrame.columns = range(self.dataFrame.shape[1])

    @loadDataFrame
    def resetIndex(self):
        """Reset index to integers"""
        self.moveIndexToColumn()
        self.dataFrame.reset_index(inplace=True, drop=True)

    @loadDataFrame
    def clearAll(self):
        """Clear entire spreadsheet"""
        self.dataFrame = pd.DataFrame()

    def moveHeaderToRow(self):
        """Move header to first row"""
        headerName = self.dataFrame.columns.name
        if headerName is None:
            headerName = self.defaultHeaderName

        if headerName not in self.dataFrame.index:
            headerRow = pd.DataFrame({headerName: self.dataFrame.columns.values}).T
            headerRow.columns = self.dataFrame.columns
            self.dataFrame = headerRow.append(self.dataFrame)

    def moveIndexToColumn(self):
        """Move index to first column row"""
        indexName = self.dataFrame.index.name
        if indexName is None:
            indexName = self.defaultIndexName

        if indexName not in self.dataFrame.columns:
            self.dataFrame.insert(0, indexName, self.dataFrame.index.values)

    cellConfig = {"padx": 5, "pady": 5, "relief": "raised", "borderwidth": 1}
    def loadDataFrame(self, df=None):
        """
        Update cells to represent current dataFrame
        """
        self.dataFrameIsLoading = True

        if df is not None:
            self.dataFrame = df
        df = self.dataFrame

        if self.columnKeys:
            size = Vec2(len(df.columns), 1)
            self.headerGrid.fillGrid(Frame, Vec2(1, 0), size, height=1)
            self.mainGrid.fillGrid(Frame, Vec2(1, 0), size, height=1)

            self.headerGrid.fillGrid(Label, Vec2(1, 1), size, values=df.columns, removeExcess=True, onClick=lambda e: self.sortColumn(cellValue=e), anchor="c")

        if self.rowKeys:
            size = Vec2(1, len(df.index))
            self.indexGrid.fillGrid(Frame, Vec2(0, 1), size, width=1)
            self.mainGrid.fillGrid(Frame, Vec2(0, 1), size, width=1)

            self.indexGrid.fillGrid(Label, Vec2(1, 1), size, values=df.index, removeExcess=True, onClick=lambda e: self.sortRow(cellValue=e))


        values = []
        for row in df.itertuples(index=False):
            values.extend(row)
        self.mainGrid.fillGrid(Label, Vec2(1, 1), Vec2(df.shape[1], df.shape[0]), values=values, removeExcess=True, color=True, **self.cellConfig)

        self.dataFrameIsLoading = False
        self.syncSizes()

    def syncSizes(self):
        if not self.dataFrameIsLoading and not self.dataFrame.columns.empty and not self.dataFrame.index.empty:
            # print(self.getMouse())
        # if self.mainGrid.getGridSize() > 0:
            self._syncColumnKeysWidth()
            self._syncRowKeysHeight()
            self._syncRowKeysWidth()
            self.app.widget.update()
            self._syncKeysScroll()

    def loadTSV(self):
        """
        Load a tsv file, configure header and index afterwards by right clicking
        """
        filetypes = [("Open a tsv file", ".tsv")]
        path = filedialog.askopenfilename(title="Select spreadsheet", filetypes=filetypes)
        if path:
            read = File.read(path)
            if read is not None:
                self.dataFrame = read
                self.loadDataFrame()

    def saveAsTSV(self):
        """Save current Data Frame as a tsv file, asks user where to put file."""
        filetypes = [("Save spreadsheet as tsv", ".tsv")]
        path = filedialog.asksaveasfilename(filetypes=filetypes, defaultextension=".tsv", title="Save spreadsheet", initialfile="Spreadsheet")
        if path:
            File.write(path, self.dataFrame, overwrite=True)

    def getMainValues(self):
        """Returns all label cell values from mainGrid in a list, going left to right row by row"""
        return [ele.getValue() for ele in self.mainGrid.getChildren() if isinstance(ele, Label)]

    def getHeaderValues(self):
        """Returns all label cell values from headerGrid in a list, going left to right row by row"""
        if self.columnKeys:
            return [ele.getValue() for ele in self.headerGrid.getChildren() if isinstance(ele, Label)]
        else:
            return list(self.dataFrame.columns)

    def getIndexValues(self):
        """Returns all label cell values from indexGrid in a list, going left to right row by row"""
        if self.rowKeys:
            return [ele.getValue() for ele in self.indexGrid.getChildren() if isinstance(ele, Label)]
        else:
            return list(self.dataFrame.index)

    def _syncKeysScroll(self, _=None):
        """Sync header and index scrolling to main grid's"""
        if self.columnKeys:
            self.headerGrid.canvas.widget.xview_moveto(self.mainGrid.canvas.widget.xview()[0])
        if self.rowKeys:
            self.indexGrid.canvas.widget.yview_moveto(self.mainGrid.canvas.widget.yview()[0])

    def _syncColumnKeysWidth(self, test=False):
        """
        Sync the widths of all cells with headers
        """
        if not self.columnKeys:
            return

        columnSize = self.headerGrid.getGridSize()
        mainSize = self.mainGrid.getGridSize()

        if columnSize.x != mainSize.x:
            raise AttributeError(f"Columns mismatch {columnSize}, {mainSize}")

        columnFrames = []
        mainFrames = []
        for pos in Vec2(1, 0).range(Vec2(columnSize.x - 1, 1)):
            columnFrame = self.headerGrid.getGridElement(pos)
            # print(columnFrame)
            columnFrame.widgetConfig(width=0)
            columnFrames.append(columnFrame)

            mainFrame = self.mainGrid.getGridElement(pos)
            # print(mainFrame)
            mainFrame.widgetConfig(width=0)
            mainFrames.append(mainFrame)

        if test:
            return

        self.app.widget.update_idletasks()

        for i, columnFrame in enumerate(columnFrames):
            mainFrame = mainFrames[i]
            columnWidth = columnFrame.widget.winfo_width()
            mainWidth = mainFrame.widget.winfo_width()
            if columnWidth > mainWidth:
                mainFrame.widgetConfig(width=columnWidth)
            else:
                columnFrame.widgetConfig(width=mainWidth)

    def _syncRowKeysHeight(self, test=False):
        """
        Sync the heights of all cells with indexes
        """
        if not self.rowKeys:
            return

        rowSize = self.indexGrid.getGridSize()
        mainSize = self.mainGrid.getGridSize()

        if rowSize.y != mainSize.y:
            raise AttributeError(f"Row mismatch {rowSize}, {mainSize}")

        rowFrames = []
        mainFrames = []
        for pos in Vec2(0, 1).range(Vec2(1, rowSize.y - 1)):
            rowFrame = self.indexGrid.getGridElement(pos)
            # print(rowFrame)
            rowFrame.widgetConfig(height=0)
            rowFrames.append(rowFrame)

            mainFrame = self.mainGrid.getGridElement(pos)
            # print(mainFrame)
            mainFrame.widgetConfig(height=0)
            mainFrames.append(mainFrame)

        if test:
            return

        self.app.widget.update_idletasks()

        for i, rowFrame in enumerate(rowFrames):
            mainFrame = mainFrames[i]
            rowHeight = rowFrame.widget.winfo_height()
            mainHeight = mainFrame.widget.winfo_height()
            if rowHeight > mainHeight:
                mainFrame.widgetConfig(height=rowHeight)
            else:
                rowFrame.widgetConfig(height=mainHeight)

    def _syncRowKeysWidth(self):
        """Set right width for index, also update filler if it exists"""
        if not self.rowKeys:
            return
        children = self.indexGrid.getChildren()
        if not children:
            return

        self.app.widget.update()  # To get right width
        rowTitleWidth = children[-1].widget.winfo_width() + 5
        self.rowKeysPageContainer.getTopElement().widgetConfig(width=rowTitleWidth)

        if self.columnKeys:
            self.columnKeysFillerLeft.widgetConfig(width=rowTitleWidth)

    def toggleAllMultilines(self, show=None):
        self.dataFrameIsLoading = True
        super().toggleAllMultilines(show=show)
        self.dataFrameIsLoading = False
        self.syncSizes()


































