"""Spreadsheet class that inherits Page"""

from generalgui import Button, Page, Label

from generallibrary.iterables import getRows


class Spreadsheet(Page):
    """
    Controls elements in a grid

    If we figure out how two frames can always have same width with grid elements inside them then each row can be an entire frame so it's easy to sort
    Should probably add row and column as arg to all elements instead of having them in packparameters
    """
    def __init__(self, parentPage=None, width=300, height=300, **parameters):
        super().__init__(parentPage=parentPage, **parameters)

        self.headerPage = Page(self, fill="x", padx=2, pack=True)
        self.cellPage = Page(self, vsb=True, hsb=True, width=width, height=height, fill="x", pack=True)

        # Keys shouldn't change order when sorting, that way we can add new rows if order is changed
        self.columnKeys = Keys()
        self.rowKeys = Keys()

        self.pack()

    def _addRows(self, obj, page):
        for rowI, row in enumerate(getRows(obj)):
            for colI, value in enumerate(row):
                label = Label(page, value, column=colI, row=rowI)
                # print(label.getWidgetConfigs())
                # label.widgetConfig(bg="red")
                # button = Button(self, value, column=colI, row=rowI, sticky="nsew")

                if rowI == 0:
                    page.getBaseWidget().columnconfigure(colI, weight=1)
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


