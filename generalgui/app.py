"""App for generalgui, controls Tk"""

from tkinter import Tk

from generalgui.shared_methods.element_page_app import Element_Page_App
from generalgui.shared_methods.page_app import Page_App


class App(Element_Page_App, Page_App):
    """
    Controls one tkinter Tk object and adds a lot of convenient features.
    """
    def __init__(self):
        self.parentPage = None
        self.widget = Tk()
        setattr(self.widget, "element", self)
        self.app = self
        self.mainlooped = False

    def mainloop(self):
        """
        Call mainloop of widget and remember it.
        """
        if not self.mainlooped:
            self.widget.mainloop()
            self.mainlooped = True

    def show(self, mainloop=True):
        """
        Create tkinter window if it's not shown. Starts mainloop if it's not started.
        """
        if not self.isShown():
            self.widget.deiconify()
        if mainloop and not self.mainlooped:
            self.mainloop()
        if not mainloop:
            self.widget.update()

    def hide(self):
        """
        Hide tkinter window if it's shown.
        """
        if self.isShown():
            self.widget.withdraw()

