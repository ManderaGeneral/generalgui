"""Spreadsheet class that inherits Page"""

from generalgui import Page, Label, Frame, Grid

from generalvector import Vec2

import pandas as pd

from tkinter import filedialog
from generalfile import File, Path


class Spreadsheet(Page):
    """
    Controls elements in a grid
    If we figure out how two frames can always have same width with grid elements inside them then each row can be an entire frame so it's easy to sort
    Should probably add row and column as arg to all elements instead of having them in packparameters
    """
    def __init__(self, parentPage=None, width=300, height=300, cellHSB=False, cellVSB=False, columnKeys=True, rowKeys=True, **parameters):
        super().__init__(parentPage=parentPage, width=width, height=height, relief="solid", borderwidth=1, resizeable=True, **parameters)

        self.cellHSB = cellHSB
        self.cellVSB = cellVSB
        self.columnKeys = columnKeys
        self.rowKeys = rowKeys

        if self.columnKeys:
            self.columnKeysPageContainer = Page(self, pack=True, fill="x")
            self.columnKeysFillerLeft = Frame(self.columnKeysPageContainer, side="left", fill="y")
            self.columnKeysGrid = Grid(self.columnKeysPageContainer, height=30, pack=True, side="left", scrollable=True, mouseScroll=False, fill="x", expand=True)
            self.columnKeysGrid.menu("Column", Remove_column=lambda: self.drop(columns=True))

        if self.rowKeys:
            self.rowKeysPageContainer = Page(self, pack=True, width=0, side="left", fill="y", pady=1)  # Pady=1 for frames in row 0 being 1 pixel high
            self.rowKeysGrid = Grid(self.rowKeysPageContainer, pack=True, side="top", width=100, scrollable=True, mouseScroll=False, fill="both", expand=True)
            self.rowKeysGrid.menu("Row", Remove_row=lambda: self.drop(rows=True))

        self.mainGrid = Grid(self, scrollable=True, hsb=cellHSB, vsb=cellVSB, pack=True, fill="both", expand=True)

        if columnKeys:
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

        self.dataFrame = pd.DataFrame()

        self.pack()

        self.menu("Spreadsheet", Save_as_tsv=self.saveAsTSV, Load_tsv_file=self.loadTSV, Reset_sort=self.resetSort)

        # self.app.createBind("<Button-1>", lambda event: print(event), name="Spreadsheet")

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

    def resetSort(self):
        """Reset the sorting of dataframe"""
        # self.dataFrame.sort_index(inplace=True)
        self.dataFrame = self.dataFrame.reindex(sorted(self.dataFrame.columns), axis=1)
        self.dataFrame = self.dataFrame.reindex(sorted(self.dataFrame.index), axis=0)
        self.loadDataFrame()

    def sort(self, event):
        """Sort a row or column by values, TypeError is silenced if there are mixed values."""
        element = event.widget.element
        rowPressed = 0 if element.parentPage == getattr(self, "columnKeysGrid", None) else 1
        value = element.getValue()

        ascending = True
        if rowPressed:
            if self.previousRowSort == value:
                ascending = False
                self.previousRowSort = None
            else:
                self.previousRowSort = value
        else:
            if self.previousColumnSort == value:
                ascending = False
                self.previousColumnSort = None
            else:
                self.previousColumnSort = value

        # In case of mixed values
        try:
            self.dataFrame.sort_values(inplace=True, axis=rowPressed, by=[value], ascending=ascending)
        except TypeError:
            return

        self.loadDataFrame()

    def drop(self, value=None, columns=False, rows=False):
        """
        Remove a column or row

        :param value: Index of either a column or a row, leave as None to use menuTarget
        :param columns:
        :param rows:
        :raises AttributeError: If columns and rows are False
        :raises ValueError: If value and menuTarget is None
        """
        if not columns and not rows:
            raise AttributeError("Columns or rows has to be set to True")

        if value is None:
            if self.app.menuTargetElement is None:
                raise ValueError("value is None and app.menuTargetElement is None")

            value = self.app.menuTargetElement.getValue()

        axis = "columns" if columns else "rows"
        self.dataFrame.drop(value, axis=axis, inplace=True)
        self.loadDataFrame()

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
            self.columnKeysGrid.fillGrid(Label, Vec2(0, 1), size, values=df.columns, removeExcess=True, onClick=lambda e: self.sort(e), **self.cellConfig)
            self.mainGrid.fillGrid(Frame, Vec2(0, 0), size, height=1)

        if self.rowKeys:
            self.rowKeysGrid.fillGrid(Label, Vec2(0, 0), Vec2(1, len(df.index)), values=df.index, removeExcess=True, onClick=lambda e: self.sort(e), **self.cellConfig)

        values = []
        for row in df.itertuples(index=False):
            values.extend(row)
        self.mainGrid.fillGrid(Label, Vec2(0, 1), Vec2(df.shape[1], df.shape[0]), values=values, removeExcess=True, **self.cellConfig)

        self._syncColumnKeysWidth()
        self._syncRowKeysWidth()
        self.app.widget.update()
        self._syncKeysScroll()

    def _syncKeysScroll(self, _=None):
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
        if not self.rowKeys:
            return

        self.app.widget.update()  # To get right width
        rowTitleWidth = self.rowKeysGrid.getChildren()[0].widget.winfo_width() + 5
        self.rowKeysPageContainer.getTopElement().widgetConfig(width=rowTitleWidth)

        if self.columnKeys:
            self.columnKeysFillerLeft.widgetConfig(width=rowTitleWidth)





































