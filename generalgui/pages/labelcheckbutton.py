"""LabelCheckbutton class that inherits Page"""

from generalgui import Label, Checkbutton, Page


class LabelCheckbutton(Page):
    """
    Controls one Label and one Entry, very minimal page.
    """
    def __init__(self, parentPage=None, value=None, default=False, **parameters):
        super().__init__(parentPage=parentPage, pady=4, **parameters)

        self.label = Label(self, value=value, side="left", padx=4)
        self.checkbutton = Checkbutton(self, default=default, side="left", padx=4, expand=True)
        self.pack()


