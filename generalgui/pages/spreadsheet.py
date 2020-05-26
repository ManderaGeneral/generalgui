"""Spreadsheet class that inherits Page"""

from generalgui import Button, Page, Label, Frame

from generallibrary.iterables import getRows
from generallibrary.types import typeChecker
from generallibrary.time import sleep

import pandas as pd


class Spreadsheet(Page):
    """
    Controls elements in a grid
    Todo: 'add' option for loadDataFrame, default to False probably
    Todo: Allow changing dataframe directly and then add a function to refresh spreadsheet

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
            self.columnKeysPage = Page(self.columnKeysPageContainer, height=30, pack=True, side="left", scrollable=True, disableMouseScroll=True, fill="x", expand=True)

        if self.rowKeys:
            self.rowKeysPageContainer = Page(self, pack=True, width=0, side="left", fill="y", pady=1)  # Pady=1 for frames in row 0 being 1 pixel high
            self.rowKeysPage = Page(self.rowKeysPageContainer, pack=True, side="top", width=100, scrollable=True, disableMouseScroll=True, fill="both", expand=True)

        self.cellPage = Page(self, scrollable=True, hsb=cellHSB, vsb=cellVSB, pack=True, fill="both", expand=True)

        if columnKeys:
            self.columnSorter = Sorter(self.columnKeysPage)
            if cellVSB:
                Frame(self.columnKeysPageContainer, side="left", width=21, fill="y")  # To fill out for existing VSB in cellPage

        if self.rowKeys:
            self.rowSorter = Sorter(self.rowKeysPage)
            if cellHSB:
                Frame(self.rowKeysPageContainer, side="top", height=20, fill="x")  # To fill out for existing HSB in cellPage. Height -1 for pady=1 in container.

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
        try:
            cells = [self.cellPage.getBaseWidget().grid_slaves(0, column)[0].element for column in range(len(headers))]
        except IndexError:
            return

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

    def _syncRowKeysWidth(self):
        if not self.rowKeys:
            return

        self.app.widget.update()  # To get right width
        rowTitleWidth = self.rowKeysPage.getChildren()[0].widget.winfo_width() + 4
        self.rowKeysPageContainer.getTopElement().widgetConfig(width=rowTitleWidth)

        if self.columnKeys:
            self.columnKeysFillerLeft.widgetConfig(width=rowTitleWidth)

    def createCell(self, page, colI, rowI, value):
        label = Label(page, value, column=colI, row=rowI, padx=5, sticky="NSEW", relief="groove", bg="gray85")
        label.createStyle("Hover", "<Enter>", "<Leave>", bg="white")
        # label.createBind("<Button-1>", lambda event: print(event))
        return label

    def loadDataFrame(self, df, add=False):
        """
        We can add an option to load df to columns instead of rows as well, then the rowKeys need to match instead of columnKeys

        :param pandas.DataFrame df:
        :param add:
        """

        existingRows = 0

        if add is False:
            if self.dataFrame is not None:
                self.clearSpreadsheet()
                self.dataFrame = None

        if self.dataFrame is None:
            if self.columnKeys:
                for i, keyValue in enumerate(df.columns):
                    Frame(self.cellPage, column=i, row=0, height=0, sticky="NSEW")
                    Frame(self.columnKeysPage, column=i, row=0, height=0, sticky="NSEW")
                    self.createCell(self.columnKeysPage, i, 1, keyValue)
            self.dataFrame = df

        else:
            if list(df.columns) != list(self.dataFrame.columns):
                raise AttributeError(f"Columns mismatch: {df.columns} != {self.dataFrame.columns}")
            if df.shape[1] != self.dataFrame.shape[1]:  # Probably not needed
                raise AttributeError(f"Columns shape mismatch: {df.shape[1]} != {self.dataFrame.shape[1]}")

            existingRows = self.dataFrame.shape[0]

            if typeChecker(self.dataFrame.index, "RangeIndex", error=False) and typeChecker(df.index, "RangeIndex", error=False):
                ignoreIndex = True
            else:
                ignoreIndex = False

            self.dataFrame = self.dataFrame.append(df, ignore_index=ignoreIndex)

        if self.rowKeys:
            for i in range(len(self.dataFrame.index) - existingRows):
                keyValue = self.dataFrame.index[existingRows + i]
                self.createCell(self.rowKeysPage, 0, existingRows + i, keyValue)

        test = []
        for rowI, row in enumerate(df.itertuples(index=False)):
            for colI, value in enumerate(row):
                test.append(self.createCell(self.cellPage, colI, 1 + existingRows + rowI, value))

        print("done")

        self._syncColumnKeysWidth()
        self._syncRowKeysWidth()
        self.app.widget.update()

    def clearSpreadsheet(self):
        self.cellPage.removeChildren()
        if self.columnKeys:
            self.columnKeysPage.removeChildren()
        if self.rowKeys:
            self.rowKeysPage.removeChildren()




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



