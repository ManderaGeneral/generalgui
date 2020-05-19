"""LabelEntry class that inherits Page"""

from generalgui import Label, Entry, Page


class LabelEntry(Page):
    """
    Controls one Label and one Entry, very minimal page.
    """
    def __init__(self, parentPage=None, value=None, default=None, width=None, **parameters):
        super().__init__(parentPage=parentPage, pady=4, **parameters)

        self.label = Label(self, value=value, side="left", padx=4)
        self.entry = Entry(self, default=default, width=width, side="left", padx=4)
        self.pack()




