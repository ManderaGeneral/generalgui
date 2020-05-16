"""Spreadsheet class that inherits Page"""

from generalgui import Label, Page

from generallibrary.iterables import getRows


class Spreadsheet(Page):
    """
    Controls elements in a grid

    If we figure out how two frames can always have same width with grid elements inside them then each row can be an entire frame so it's easy to sort
    Should probably add row and column as arg to all elements instead of having them in packparameters
    """
    def __init__(self, parentPage=None, width=640, height=640, **packParameters):
        super().__init__(parentPage=parentPage, width=width, height=height, **packParameters)
        self.pack()

        # Keys shouldn't change order when sorting, that way we can add new rows if order is changed
        self.columnKeys = Keys()
        self.rowKeys = Keys()


    def addRows(self, obj):
        for rowI, row in enumerate(getRows(obj)):
            for colI, value in enumerate(row):
                label = Label(self, value, column=colI, row=rowI)


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


