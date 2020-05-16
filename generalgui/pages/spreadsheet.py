"""Spreadsheet class that inherits Page"""

from generalgui import Label, Page

from generallibrary.iterables import getRows


class Spreadsheet(Page):
    """
    Controls elements in a grid
    """
    def __init__(self, parentPage=None, rows=None, **packParameters):
        super().__init__(parentPage=parentPage, **packParameters)
        self.pack()

        # Keys shouldn't change order when sorting, that way we can add new rows if order is changed
        self.columnKeys = Keys()
        self.rowKeys = Keys()

        if rows:
            self.addRows(rows)

    def addRows(self, obj):
        for row in getRows(obj):
            print(row)


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


