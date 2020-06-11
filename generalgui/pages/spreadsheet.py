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
    """Helper for index and header decorators"""
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
        spreadsheet = grid.getFirstParentClass("Spreadsheet")
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
    Controls elements in a grid
    If we figure out how two frames can always have same width with grid elements inside them then each row can be an entire frame so it's easy to sort
    Should probably add row and column as arg to all elements instead of having them in packparameters

    Keys -> Header / Index
    Header (df.columns) -> Columns
    Index (df.index) -> Rows
    """
    def __init__(self, parentPage=None, width=300, height=300, cellHSB=False, cellVSB=False, columnKeys=True, rowKeys=True, **parameters):
        super().__init__(parentPage=parentPage, width=width, height=height, relief="solid", borderwidth=1, resizeable=True, **parameters)

        menus = {
            "Row": {
                "Index:": self.getIndexName,
                "Row:": self.getRowName,
                "Average:": self.getRowAverage,
                "Remove_row": self.dropRow,
                "Make_row_header": self.makeRowHeader
            },
            "Column": {
                "Header:": self.getHeaderName,
                "Column:": self.getColumnName,
                "Average:": self.getColumnAverage,
                "Remove_column": self.dropColumn,
                "Make_column_index": self.makeColumnIndex
            }
        }

        self.cellHSB = cellHSB
        self.cellVSB = cellVSB
        self.columnKeys = columnKeys
        self.rowKeys = rowKeys

        if self.columnKeys:
            self.columnKeysPageContainer = Page(self, pack=True, fill="x")
            self.columnKeysFillerLeft = Frame(self.columnKeysPageContainer, side="left", fill="y")
            self.columnKeysGrid = Grid(self.columnKeysPageContainer, height=30, pack=True, side="left", scrollable=True, mouseScroll=False, fill="x", expand=True)
            self.columnKeysGrid.menu("Column", **menus["Column"])

        if self.rowKeys:
            self.rowKeysPageContainer = Page(self, pack=True, width=0, side="left", fill="y", pady=1)  # Pady=1 for frames in row 0 being 1 pixel high
            self.rowKeysGrid = Grid(self.rowKeysPageContainer, pack=True, side="top", width=100, scrollable=True, mouseScroll=False, fill="both", expand=True)
            self.rowKeysGrid.menu("Row", **menus["Row"])

        self.mainGrid = Grid(self, scrollable=True, hsb=cellHSB, vsb=cellVSB, pack=True, fill="both", expand=True)

        if self.columnKeys:
            self.previousColumnSort = None
            if cellVSB:
                Frame(self.columnKeysPageContainer, side="left", width=21, fill="y")  # To fill out for existing VSB in mainGrid

        if self.rowKeys:
            self.previousRowSort = None
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

                  Reset_header=self.resetHeader,
                  Reset_index=self.resetIndex,

                  Sort_header=self.sortHeader,
                  Sort_index=self.sortIndex,

                  Clear_all=self.clearAll)


    defaultHeaderName = "headers"
    defaultIndexName = "indexes"

    @indexValue
    def getRowAverage(self, cellValue=None):
        """Return the row average"""
        try:
            return np.average(self.dataFrame.loc[[cellValue]].values[0])
        except TypeError:
            return None

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
    def sortHeader(self):
        """Sort headers in dataframe"""
        try:
            self.dataFrame = self.dataFrame.reindex(sorted(self.dataFrame.columns), axis=1)
        except TypeError:
            pass

    @loadDataFrame
    def sortIndex(self):
        """Sort index in dataframe"""
        try:
            self.dataFrame = self.dataFrame.reindex(sorted(self.dataFrame.index), axis=0)
        except TypeError:
            pass

    @loadDataFrame
    @indexValue
    def sortRow(self, cellValue=None):
        """Sort a row in dataframe"""
        ascending = True
        if self.previousRowSort == cellValue:
            ascending = False
            self.previousRowSort = None
        else:
            self.previousRowSort = cellValue
        try:  # In case of mixed values
            self.dataFrame.sort_values(inplace=True, axis=1, by=[cellValue], ascending=ascending)
        except TypeError:
            return

    @loadDataFrame
    @headerValue
    def sortColumn(self, cellValue=None):
        """Sort a column in dataframe"""
        ascending = True
        if self.previousColumnSort == cellValue:
            ascending = False
            self.previousColumnSort = None
        else:
            self.previousColumnSort = cellValue
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

    @headerValue
    @loadDataFrame
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
        """Move index to column row"""
        indexName = self.dataFrame.index.name
        if indexName is None:
            indexName = self.defaultIndexName

        if indexName not in self.dataFrame.columns:
            self.dataFrame.insert(0, indexName, self.dataFrame.index.values)

    cellConfig = {"padx": 5, "relief": "groove", "bg": "gray85"}
    def loadDataFrame(self, df=None):
        """
        Update cells to represent current dataFrame
        """
        if df is not None:
            self.dataFrame = df
        df = self.dataFrame

        if self.columnKeys:
            size = Vec2(len(df.columns), 1)
            self.columnKeysGrid.fillGrid(Frame, Vec2(0, 0), size, height=1)
            self.columnKeysGrid.fillGrid(Label, Vec2(0, 1), size, values=df.columns, removeExcess=True,
                                         onClick=lambda e: self.sortColumn(e), **self.cellConfig)
            self.mainGrid.fillGrid(Frame, Vec2(0, 0), size, height=1)

        if self.rowKeys:
            self.rowKeysGrid.fillGrid(Label, Vec2(0, 1), Vec2(1, len(df.index)), values=df.index, removeExcess=True,
                                      onClick=lambda e: self.sortRow(e), **self.cellConfig)

        values = []
        for row in df.itertuples(index=False):
            values.extend(row)
        self.mainGrid.fillGrid(Label, Vec2(0, 1), Vec2(df.shape[1], df.shape[0]), values=values, removeExcess=True, **self.cellConfig)

        self._syncColumnKeysWidth()
        self._syncRowKeysWidth()
        self.app.widget.update()
        self._syncKeysScroll()

    def loadTSV(self):
        """
        Load a tsv file

        HERE ** Working, but headers can be messed up
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

    def _syncKeysScroll(self, _=None):
        """Sync header and index scrolling to main grid's"""
        if self.columnKeys:
            self.columnKeysGrid.canvas.widget.xview_moveto(self.mainGrid.canvas.widget.xview()[0])
        if self.rowKeys:
            self.rowKeysGrid.canvas.widget.yview_moveto(self.mainGrid.canvas.widget.yview()[0])

    def _syncColumnKeysWidth(self, test=False):
        """
        Sync the widths of all cells with headers
        """
        if not self.columnKeys:
            return

        columnSize = self.columnKeysGrid.getGridSize()
        mainSize = self.mainGrid.getGridSize()

        if columnSize.x != mainSize.x:
            raise AttributeError(f"Columns mismatch {columnSize}, {mainSize}")

        columnFrames = []
        mainFrames = []
        for pos in Vec2(0,0).range(Vec2(columnSize.x, 1)):
            columnFrame = self.columnKeysGrid.getGridElement(pos)
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

    def _syncRowKeysWidth(self):
        """Set right width for index, also update filler if it exists"""
        if not self.rowKeys:
            return
        children = self.rowKeysGrid.getChildren()
        if not children:
            return

        self.app.widget.update()  # To get right width
        rowTitleWidth = children[0].widget.winfo_width() + 5
        self.rowKeysPageContainer.getTopElement().widgetConfig(width=rowTitleWidth)

        if self.columnKeys:
            self.columnKeysFillerLeft.widgetConfig(width=rowTitleWidth)





































