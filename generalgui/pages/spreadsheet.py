"""Spreadsheet class that inherits Page"""

from generalgui import Button, Page, Label, Frame, Grid

from generalvector import Vec2

import pandas as pd


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

        if self.rowKeys:
            self.rowKeysPageContainer = Page(self, pack=True, width=0, side="left", fill="y", pady=1)  # Pady=1 for frames in row 0 being 1 pixel high
            self.rowKeysGrid = Grid(self.rowKeysPageContainer, pack=True, side="top", width=100, scrollable=True, mouseScroll=False, fill="both", expand=True)

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

        # Keys shouldn't change order when sorting, that way we can add new rows if order is changed
        self.dataFrame = pd.DataFrame()

        self.pack()



        # HERE ** Menu prototype
        self.app.menu = page = Page(self.app, relief="solid", borderwidth=1)
        Button(page, "Menu", lambda: print(5))
        Button(page, "Menu", lambda: print(2))



        # self.app.createBind("<Button-1>", lambda event: print(event), name="Spreadsheet")

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
            self.columnKeysGrid.fillGrid(Label, Vec2(0, 1), size, values=df.columns, removeExcess=True, onClick=lambda e: self.sortByColumn(e), **self.cellConfig)
            self.mainGrid.fillGrid(Frame, Vec2(0, 0), size, height=1)

        if self.rowKeys:
            self.rowKeysGrid.fillGrid(Label, Vec2(0, 0), Vec2(1, len(df.index)), values=df.index, removeExcess=True, onClick=lambda e: self.sortByColumn(e), **self.cellConfig)

        values = []
        for row in df.itertuples(index=False):
            values.extend(row)
        self.mainGrid.fillGrid(Label, Vec2(0, 1), Vec2(df.shape[1], df.shape[0]), values=values, removeExcess=True, **self.cellConfig)

        self._syncColumnKeysWidth()
        self._syncRowKeysWidth()
        self.app.widget.update()
        self._syncKeysScroll()

    def sortByColumn(self, event):
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

        try:
            self.dataFrame.sort_values(inplace=True, axis=rowPressed, by=[value], ascending=ascending)
        except TypeError:
            return

        self.loadDataFrame()






































