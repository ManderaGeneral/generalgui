"""App for generalgui, controls Tk"""

from tkinter import Tk
from tkinter import font

from generalgui.shared_methods.element_page_app import Element_Page_App
from generalgui.shared_methods.element_app import Element_App
from generalgui.shared_methods.page_app import Page_App
from generalgui.shared_methods.scroller import Scroller
from generalgui.shared_methods.resizer import Resizer


from generalvector import Vec2

from generallibrary.time import Timer


class App(Element_Page_App, Element_App, Page_App, Scroller, Resizer):
    """
    Controls one tkinter Tk object and adds a lot of convenient features.
    """
    def __init__(self):
        Element_App.__init__(self)

        self.widget = Tk()
        setattr(self.widget, "element", self)
        self.app = self
        self.mainlooped = False


        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(size=10, family="Helvetica")
        self.widget.option_add("*Font", default_font)
        # print(default_font.actual())


        Scroller.__init__(self)
        Resizer.__init__(self)


        def debug(widget):
            print(
                widget.winfo_height(),
                widget.bbox("all"),
                widget["scrollregion"],
                widget,
            )

        # self.createBind("<Button-1>", lambda event: debug(event.widget))

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

