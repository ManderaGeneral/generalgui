"""Spreadsheet class that inherits Page"""

from generalgui import Button, Page, Label, Frame

from generallibrary.iterables import getRows
from generallibrary.time import Timer

class Spreadsheet(Page):
    """
    Controls elements in a grid

    If we figure out how two frames can always have same width with grid elements inside them then each row can be an entire frame so it's easy to sort
    Should probably add row and column as arg to all elements instead of having them in packparameters
    """
    def __init__(self, parentPage=None, width=500, height=500, **parameters):
        super().__init__(parentPage=parentPage, width=width, height=height, relief="solid", borderwidth=1, **parameters)

        self.topPage = Page(self, pack=True, height=30, fill="x", cursor="hand2")
        self.headerPage = Page(self.topPage, pack=True, side="left", scrollable=True, fill="x", expand=True)
        Frame(self.topPage, side="left", width=21, fill="y")  # To fill out for existing VSB in cellPage

        self.cellPage = Page(self, vsb=True, hsb=True, pack=True, fill="both", expand=True)
        self.cellPage.hsb.createBind("<B1-Motion>", lambda event: self._syncHeaderScroll(event), add=True)  # Make scrollbar affect headerPage too

        self.app.createBind("<B3-Motion>", self._syncHeaderScroll)



        # Keys shouldn't change order when sorting, that way we can add new rows if order is changed
        self.columnKeys = Keys()
        self.rowKeys = Keys()

        self.pack()

    def _syncHeaderScroll(self, _):
        self.headerPage.canvas.widget.xview_moveto(self.cellPage.canvas.widget.xview()[0])

    def syncWidths(self):
        """
        Sync the widths of all cells with headers
        """
        headers = [child for child in self.headerPage.getChildren() if isinstance(child, Frame)]
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

    def _addRowsToPage(self, obj, page):
        for rowI, row in enumerate(getRows(obj)):
            for colI, value in enumerate(row):
                label = Label(page, value, column=colI, row=rowI + 1, sticky="NSEW", relief="groove", bg="gray85")
                label.createStyle("Hover", "<Enter>", "<Leave>", bg="white")
                label.createBind("<Button-1>", lambda event: print(event))
                if rowI == 0:
                    Frame(page, column=colI, row=0, height=0, sticky="NSEW")

    def addRows(self, obj):
        """
        Add rows to cells
        """
        self._addRowsToPage(obj, self.cellPage)

    def headerRows(self, obj):
        """
        Add rows to header
        """
        self._addRowsToPage(obj, self.headerPage)

class Keys:
    """
    Used for columns and rows

    When changing columnKeys' sortKey it affects rowKeys' sortedKeys and vice versa.
    """
    def __init__(self):
        self.keys = []
        self.sortedKeys = []  # Contains same elements as keys but in a possibly different order
        self.sortKey = None
        self.reversed = False


