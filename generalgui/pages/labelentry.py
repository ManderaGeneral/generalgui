"""LabelEntry class that inherits Page"""

from generalgui import Label, Entry, Page


class LabelEntry(Page):
    """
    Controls one Label and one Entry, very minimal page.
    """
    def __init__(self, parentPage=None, text=None, default=None, width=None, **packParameters):
        super().__init__(parentPage=parentPage, **packParameters)

        self.label = Label(self, text, side="left")
        self.label.widgetConfig(padx=4)

        self.entry = Entry(self, default=default, width=width, side="left")
        self.label.widgetConfig(padx=4)

        self.widgetConfig(pady=4)


