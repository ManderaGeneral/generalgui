"""App for generalgui, controls Frame"""

from generallibrary.types import typeChecker
import tkinter as tk
from generalgui.shared_methods.element_page_app import Element_Page_App
from generalgui.shared_methods.element_page import Element_Page
from generalgui.shared_methods.page_app import Page_App

class Page(Element_Page, Element_Page_App, Page_App):
    """
    Controls one tkinter Frame and adds a lot of convenient features.
    Hidden by default.
    """
    def __init__(self, parentPage=None, removeSiblings=False, width=None, height=None):
        """

        :param parentPage:
        :param removeSiblings:
        """

        typeChecker(parentPage, (None, Page, App))

        if parentPage is None:
            parentPage = App()
        elif removeSiblings:
            parentPage.removeChildren()

        if height is None and width is None:
            widget = tk.Frame(parentPage.getBaseWidget())
        else:
            widget = self._getScrollableWidget(parentPage, width, height)

        super().__init__(parentPage=parentPage, widget=widget)


    def _getScrollableWidget(self, parentPage, width, height):
        canvas = tk.Canvas(parentPage.getBaseWidget(), width=width, height=height)
        canvas.pack_propagate(0)
        self.setPackParameters(canvas, fill="both", expand=True)

        frame = tk.Frame(canvas)
        self.setPackParameters(frame, side="left", fill="both", expand=True)

        vsb = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")

        hsb = tk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=hsb.set)
        hsb.pack(side="bottom", fill="x")

        canvas.create_window((4, 4), window=frame, anchor="nw", tags="self.canvas")

        canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

        setattr(canvas, "widget", frame)
        setattr(frame, "element", self)
        return canvas


from generalgui.app import App


