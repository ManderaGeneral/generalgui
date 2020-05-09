"""App for generalgui, controls Tk"""
from tkinter import Tk
from generalgui.shared_methods import Element_Page_App, Page_App

class App(Element_Page_App, Page_App):
    """
    Controls one tkinter Tk object and adds a lot of convenient features.
    """
    def __init__(self):
        self.parentPage = None
        self.widget = Tk()
        self.app = self

        self.mainlooped = False

    def show(self):
        """
        Create tkinter window if it's not shown. Starts mainloop if it's not started.
        """
        if not self.isShown():
            self.widget.deiconify()

            if not self.mainlooped:
                self.widget.mainloop()
                self.mainlooped = True

    def hide(self):
        """
        Hide tkinter window if it's shown.
        """
        if self.isShown():
            self.widget.withdraw()

