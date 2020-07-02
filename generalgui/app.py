"""App for generalgui, controls Tk"""

from tkinter import Tk
from tkinter import font

from generalgui.shared_methods.element_page_app import Element_Page_App
from generalgui.shared_methods.element_app import Element_App
from generalgui.shared_methods.page_app import Page_App
from generalgui.shared_methods.scroller import Scroller
from generalgui.shared_methods.resizer import Resizer
from generalgui.shared_methods.menu import Menu_App

from generallibrary.iterables import getFreeIndex
from generallibrary.types import typeChecker


class tkTk(Tk):
    def after_helper(self, func, index):
        del self.element.afters[index]
        return func()

    def after(self, ms, func=None, *args):
        identifier = super().after(ms, lambda i=getFreeIndex(self.element.afters): self.after_helper(func, i), *args)
        self.element.afters[getFreeIndex(self.element.afters)] = identifier

apps = []
class App(Element_Page_App, Element_App, Page_App, Scroller, Resizer, Menu_App):
    """
    Controls one tkinter Tk object and adds a lot of convenient features.
    """
    def __init__(self):
        Element_App.__init__(self)
        Element_Page_App.__init__(self)

        apps.append(self)

        self.widget = tkTk()
        self.afters = {}

        setattr(self.widget, "element", self)
        self.app = self
        self.mainlooped = False

        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(size=10, family="Helvetica")
        self.widget.option_add("*Font", default_font)
        # print(default_font.actual())

        self.Element = Element

        self.Page = gui.Page
        self.Button = gui.Button
        self.Canvas = gui.Canvas
        self.Checkbutton = gui.Checkbutton
        self.Entry = gui.Entry
        self.Frame = gui.Frame
        self.Label = gui.Label
        self.OptionMenu = gui.OptionMenu
        self.Scrollbar = gui.Scrollbar

        self.LabelCheckbutton = gui.LabelCheckbutton
        self.LabelEntry = gui.LabelEntry

        Scroller.__init__(self)
        Resizer.__init__(self)
        Menu_App.__init__(self)

        self.menu("App", Rainbow=self.rainbow, Reset=lambda: self.rainbow(True))

        # Mainly to remove focus from entries but had some mostly nice side-effects
        def setFocus(e):
            e.widget.focus_set()
        self.createBind("<Button-1>", setFocus)

        # def cleanAfters():
        #     for identifier in self.afters.values():
        #         print(identifier)
        #         self.widget.after_cancel(identifier)
        # self.createBind("<Destroy>", cleanAfters)

    @classmethod
    def getApps(cls):
        return apps

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

    def remove(self):
        apps.remove(self)
        # self.widget.update()
        self.widget.quit()



import generalgui as gui
from generalgui.element import Element

