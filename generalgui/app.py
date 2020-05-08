
from tkinter import Tk
from generalgui.page import Page

# Inherit Page?
class App(Page):
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

    def getParentPages(self, includeSelf=False):
        raise BlockingIOError("This method is disabled in App")


