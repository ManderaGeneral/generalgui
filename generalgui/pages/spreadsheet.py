"""Spreadsheet class that inherits Page"""

from generalgui import Button, Page, Label, Frame

from generallibrary.iterables import getRows
from generallibrary.types import typeChecker

import pandas as pd


class Spreadsheet(Page):
    """
    Controls elements in a grid

    If we figure out how two frames can always have same width with grid elements inside them then each row can be an entire frame so it's easy to sort
    Should probably add row and column as arg to all elements instead of having them in packparameters
    """
    def __init__(self, parentPage=None, width=600, height=600, cellHSB=False, cellVSB=False, columnKeys=True, rowKeys=True, **parameters):
        super().__init__(parentPage=parentPage, width=width, height=height, relief="solid", borderwidth=1, **parameters)

        self.columnKeys = columnKeys
        self.rowKeys = rowKeys

        if self.columnKeys:
            self.columnKeysPageContainer = Page(self, pack=True, height=30, fill="x")
            self.columnKeysFillerLeft = Frame(self.columnKeysPageContainer, side="left", fill="y")  # To fill out for existing rowHeaderPage
            self.columnKeysPage = Page(self.columnKeysPageContainer, pack=True, side="left", scrollable=True, fill="x", expand=True, cursor="hand2")

        if self.rowKeys:
            self.rowKeysPageContainer = Page(self, pack=True, height=200, side="left", fill="y")
            self.rowKeysPage = Page(self.rowKeysPageContainer, pack=True, side="top", scrollable=True, fill="both", expand=True, cursor="hand2")

        self.cellPage = Page(self, scrollable=True, hsb=cellHSB, vsb=cellVSB, pack=True, fill="both", expand=True)


        if columnKeys:
            self.columnSorter = Sorter(self.columnKeysPage)
            if cellVSB:
                Frame(self.columnKeysPageContainer, side="left", width=21, fill="y")  # To fill out for existing VSB in cellPage
        if self.rowKeys:
            self.rowSorter = Sorter(self.rowKeysPage)
            if cellHSB:
                Frame(self.rowKeysPageContainer, side="top", height=21, fill="x")  # To fill out for existing HSB in cellPage

        # Update headers whenever canvas moves (Manual scrollbar, mousewheel and right-click drag)
        if self.rowKeys or self.columnKeys:
            self.cellPage.canvasFrame.createBind("<Configure>", lambda event: self._syncKeysScroll(event), add=True)

        # Keys shouldn't change order when sorting, that way we can add new rows if order is changed
        self.dataFrame = None

        self.pack()

    def _syncKeysScroll(self, _):
        if self.columnKeys:
            self.columnKeysPage.canvas.widget.xview_moveto(self.cellPage.canvas.widget.xview()[0])
        if self.rowKeys:
            self.rowKeysPage.canvas.widget.yview_moveto(self.cellPage.canvas.widget.yview()[0])

    def _syncColumnKeysWidth(self):
        """
        Sync the widths of all cells with headers
        """
        if not self.columnKeys:
            return

        headers = [child for child in self.columnKeysPage.getChildren() if isinstance(child, Frame)]
        cells = [self.cellPage.getBaseWidget().grid_slaves(0, column)[0].element for column in range(len(headers))]

        for header in headers:
            header.widgetConfig(width=0)
        for cell in cells:
            cell.widgetConfig(width=0)

        self.app.widget.update()

        headerWidths = [header.widget.winfo_width() for header in headers]
        cellWidths = [cell.widget.winfo_width() for cell in cells]

        for column in range(len(headers)):
            if headerWidths[column] > cellWidths[column]:
                cells[column].widgetConfig(width=headerWidths[column])
            elif cellWidths[column] > headerWidths[column]:
                headers[column].widgetConfig(width=cellWidths[column])

        # Grid doesn't update for some reason when chaning width of cells manually, so force it to here
        self.getTopElement().widgetConfig(width=0)
        self.app.widget.update()
        self.getTopElement().widgetConfig(width=self.parameters["width"])

    def _syncRowKeysWidth(self):
        if not self.rowKeys:
            return

        rowTitleWidth = self.rowKeysPage.getChildren()[0].widget.winfo_width() + 4
        self.rowKeysPageContainer.getTopElement().widgetConfig(width=rowTitleWidth)

        if self.columnKeys:
            self.columnKeysFillerLeft.widgetConfig(width=rowTitleWidth)

    def createCell(self, page, colI, rowI, value):
        label = Label(page, value, column=colI, row=rowI, padx=5, sticky="NSEW", relief="groove", bg="gray85")
        label.createStyle("Hover", "<Enter>", "<Leave>", bg="white")
        label.createBind("<Button-1>", lambda event: print(event))


    def loadDataFrame(self, df):
        """
        We can add an option to load df to columns instead of rows as well, then the rowKeys need to match instead of columnKeys

        :param pandas.DataFrame df:
        """

        # print(df.index, df.columns)

        if self.dataFrame is None:
            if self.columnKeys:
                for i, keyValue in enumerate(df.columns):
                    Frame(self.cellPage, column=i, row=0, height=0, sticky="NSEW")
                    Frame(self.columnKeysPage, column=i, row=0, height=0, sticky="NSEW")
                    self.createCell(self.columnKeysPage, i, 1, keyValue)
            existingRows = 0
            self.dataFrame = df

        else:
            if list(df.columns) != list(self.dataFrame.columns):
                raise AttributeError(f"Columns mismatch {df.columns} != {self.dataFrame.columns}")

            existingRows = self.dataFrame.shape[0]

            if typeChecker(self.dataFrame.index, "RangeIndex", error=False) and typeChecker(df.index, "RangeIndex", error=False):
                ignoreIndex = True
            else:
                ignoreIndex = False

            self.dataFrame = self.dataFrame.append(df, ignore_index=ignoreIndex)

        if self.rowKeys:
            for i in range(len(self.dataFrame.index) - existingRows):
                keyValue = self.dataFrame.index[existingRows + i]
                # HERE ** Dunno why cell has 0 width first time
                print(keyValue)
                self.createCell(self.rowKeysPage, 0, existingRows + i, keyValue)


        for rowI, row in enumerate(df.itertuples(index=False)):
            for colI, value in enumerate(row):
                self.createCell(self.cellPage, colI, 1 + existingRows + rowI, value)

        self._syncColumnKeysWidth()
        self._syncRowKeysWidth()





    def addRows(self, obj):
        """
        Add rows to cells
        """
        rows = getRows(obj)
        self._addRowsToPage(rows, self.cellPage)

        headers = [[i for i in range(len(rows[0]))]]
        rowTitles = [[i] for i in range(len(rows))]

        self._addRowsToPage(headers, self.columnKeysPage)
        self._addRowsToPage(rowTitles, self.rowKeysPage)

        self._syncColumnKeysWidth()
        self._syncRowKeysWidth()

    def _addRowsToPage(self, rows, page):
        for rowI, row in enumerate(rows):
            for colI, value in enumerate(row):
                label = Label(page, value, column=colI, row=rowI + 1, padx=5, sticky="NSEW", relief="groove", bg="gray85")
                label.createStyle("Hover", "<Enter>", "<Leave>", bg="white")
                label.createBind("<Button-1>", lambda event: print(event))

                # Fix this. It stacks atm
                if rowI == 0:
                    Frame(page, column=colI, row=0, height=0, sticky="NSEW")

class Sorter:
    """
    Used for columns and rows

    When changing columnKeys' sortKey it affects rowKeys' sortedKeys and vice versa.
    """
    def __init__(self, page):
        self.page = page
        self.keys = []
        self.sortedKeys = []  # Contains same elements as keys but in a possibly different order
        self.sortKey = None
        self.reversed = False



