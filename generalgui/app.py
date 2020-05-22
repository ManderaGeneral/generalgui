"""App for generalgui, controls Tk"""

from tkinter import Tk
from tkinter import font

from generalgui.shared_methods.element_page_app import Element_Page_App
from generalgui.shared_methods.element_app import Element_App
from generalgui.shared_methods.page_app import Page_App

from generalvector import Vec2

from generallibrary.time import Timer


class App(Element_Page_App, Element_App, Page_App):
    """
    Controls one tkinter Tk object and adds a lot of convenient features.
    """
    def __init__(self):
        super().__init__()
        self.widget = Tk()
        setattr(self.widget, "element", self)
        self.app = self
        self.mainlooped = False

        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(size=10, family="Helvetica")
        self.widget.option_add("*Font", default_font)
        # print(default_font.actual())

        self.scrollWheelTarget = None
        self.scrollButtonEnabled = False
        self.startCoords = None
        self.createBind("<MouseWheel>", self.scrollWheel)
        self.createBind("<Button-3>", self.scrollButton)
        self.createBind("<ButtonRelease-3>", self.scrollButtonRelease)
        self.createBind("<B3-Motion>", self.scrollButtonMove)

    def scrollButton(self, event):
        self.startCoords = Vec2(event.x_root, event.y_root)
        if self.scrollWheelTarget is not None:
            self.scrollButtonEnabled = True

    def scrollButtonRelease(self, event):
        self.scrollButtonEnabled = False

    def scrollButtonMove(self, event):
        if self.scrollButtonEnabled:
            coords = Vec2(event.x_root, event.y_root)
            mouseDiff = coords - self.startCoords
            self.startCoords = coords

            self.scrollWheelTarget.widget.xview_scroll(-mouseDiff.x, "units")
            self.scrollWheelTarget.widget.yview_scroll(-mouseDiff.y, "units")


    def scrollWheel(self, event):
        """
        When scrolling anywhere on App
        """
        if self.scrollWheelTarget is not None:
            self.scrollWheelTarget.widget.yview_scroll(round(event.delta / -1), "units")

    def setScrollTarget(self, element):
        """
        Targets an element to be scrolled if mousewheel is moved
        """
        self.scrollWheelTarget = element

    def removeScrollTarget(self, element):
        """
        Removes mouse wheel target
        """
        if element == self.scrollWheelTarget:
            self.scrollWheelTarget = None

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

