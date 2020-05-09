
from tkinter import Tk

from generalgui.shared_methods import Element_Page_App, Page_App

# Inherit Page?
class App(Element_Page_App, Page_App):
    """
    Container for Tk() object with a lot of convenient features.
    """
    def __init__(self):
        self.parentPage = None
        self.widget = Tk()
        self.app = self

        self.mainlooped = False

    def show(self):
        if not self.isShown():
            self.widget.deiconify()

            if not self.mainlooped:
                self.widget.mainloop()
                self.mainlooped = True

    def hide(self):
        if self.isShown():
            self.widget.withdraw()


