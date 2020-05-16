"""LabelCheckbutton class that inherits Page"""

from generalgui import Label, Checkbutton, Page


class LabelCheckbutton(Page):
    """
    Controls one Label and one Entry, very minimal page.
    """
    def __init__(self, parentPage=None, value=None, default=False, **packParameters):
        super().__init__(parentPage=parentPage, **packParameters)
        self.pack()

        self.label = Label(self, value, side="left")

        self.checkbutton = Checkbutton(self, default=default, side="left")

        self.widgetConfig(pady=4, padx=4)




