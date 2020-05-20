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
        super().__init__(parentPage=parentPage, width=width, height=height, **parameters)

        self.topPage = Page(self, pack=True, height=25, fill="x")

        self.headerPage = Page(self.topPage, pack=True, side="left", fill="both")
        # self.headerPage.getTopWidget().grid_propagate(0)

        # self.headerPage = Page(self, fill="x", padx=2, pack=True)

        self.cellPage = Page(self, vsb=True, hsb=True, pack=True)

        self.cellPage.baseElement.createBind("<Configure>", lambda event: self._configureBind(event), add=True)

        # Keys shouldn't change order when sorting, that way we can add new rows if order is changed
        self.columnKeys = Keys()
        self.rowKeys = Keys()

        self.pack()

    def syncWidths(self):
        headers = [child for child in self.headerPage.getChildren() if isinstance(child, Frame)]
        cells = [self.cellPage.getBaseWidget().grid_slaves(0, column)[0].element for column in range(len(headers))]


        for header in headers:
            header.widgetConfig(width=0)
        for cell in cells:
            cell.widgetConfig(width=0)

        self.app.widget.update()

        headerWidths = [header.widget.winfo_width() for header in headers]
        cellWidths = [cell.widget.winfo_width() for cell in cells]

        print(headerWidths)
        print(cellWidths)

        for column in range(len(headers)):
            if headerWidths[column] > cellWidths[column]:
                print("cell", headerWidths[column] - cellWidths[column])
                # cells[column].widgetConfig(padx=round((headerWidths[column] - cellWidths[column]) / 2))
                cells[column].widgetConfig(width=headerWidths[column])
            elif cellWidths[column] > headerWidths[column]:
                print("headers", cellWidths[column] - headerWidths[column])
                # headers[column].widgetConfig(padx=round((cellWidths[column] - headerWidths[column]) / 2))
                headers[column].widgetConfig(width=cellWidths[column])

        # widget = cells[2].widget
        # print(widget.winfo_width())
        #
        # widget.config(padx=13)
        # self.app.widget.update()
        # print(widget.winfo_width())
        #
        # widget.config(padx=50)
        # self.app.widget.update()
        # print(widget.winfo_width())

        # print(headerWidths)
        # print(cellWidths)


    def _configureBind(self, event):
        pass
        # self.headerPage.widgetConfig(width=event.width)
        # widget = self.headerPage.getChildren()[0].widget
        # widget2 = self.headerPage.getChildren()[1].widget
        # width = widget.winfo_width()
        # widget.config(width=width)

    def _addRows(self, obj, page):
        for rowI, row in enumerate(getRows(obj)):
            for colI, value in enumerate(row):
                Label(page, value, column=colI, row=rowI + 1, sticky="NSEW")
                # print(label.getWidgetConfigs())
                # label.widgetConfig(bg="red")
                # button = Button(self, value, column=colI, row=rowI, sticky="nsew")

                if rowI == 0:
                    # print("col", colI)
                    Frame(page, column=colI, row=0, height=5, sticky="NSEW")
                #     page.getBaseWidget().columnconfigure(colI, weight=1)


        # self.cellPage.widget.configure(scrollregion=self.cellPage.widget.bbox("all"))

    def addRows(self, obj):
        self._addRows(obj, self.cellPage)

    def headerRows(self, obj):
        self._addRows(obj, self.headerPage)

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


