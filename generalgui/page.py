"""App for generalgui, controls Frame"""

import tkinter as tk

from generallibrary.types import typeChecker

from generalgui.shared_methods.element_page import Element_Page
from generalgui.shared_methods.element_page_app import Element_Page_App
from generalgui.shared_methods.page_app import Page_App


class Page(Element_Page, Element_Page_App, Page_App):
    """
    Controls one tkinter Frame and adds a lot of convenient features.
    Hidden by default.
    """
    def __init__(self, parentPage=None, removeSiblings=False, width=None, height=None, vsb=True, hsb=True, **packParameters):
        """
        Create a new page that is hidden by default and controls one frame. Becomes scrollable if width or height is defined.

        :param App or Page or None parentPage: Parent page, can be App, Page or None (Creates new App).
        :param removeSiblings: Remove all siblings on creations, to easily update a page for example by replacing it.
        :param None or int width: Width in pixels
        :param None or int height: Width in pixels
        :param vsb: Vertical scrollbar if page is scrollable.
        :param hsb: Horiziontal scrollbar if page is scrollable
        :param packParameters: Parameters given to page's tkinter Frame when being packed.
        """

        typeChecker(parentPage, (None, Page, App))

        if parentPage is None:
            parentPage = App()
        elif removeSiblings:
            parentPage.removeChildren()

        if height is None and width is None:
            widget = tk.Frame(parentPage.getBaseWidget())
        else:
            widget = self._getScrollableWidget(parentPage, width, height, vsb, hsb)

        self.setPackParameters(widget, **packParameters)

        super().__init__(parentPage=parentPage, widget=widget)


    def _getScrollableWidget(self, parentPage, width, height, vsb, hsb):
        canvas = tk.Canvas(parentPage.getBaseWidget(), width=width, height=height)
        canvas.pack_propagate(0)
        self.setPackParameters(canvas, fill="both", expand=True)

        frame = tk.Frame(canvas)
        self.setPackParameters(frame, side="left", fill="both", expand=True)

        if vsb:
            verticalScrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
            canvas.configure(yscrollcommand=verticalScrollbar.set)
            verticalScrollbar.pack(side="right", fill="y")

        if hsb:
            horizontalScrollbar = tk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
            canvas.configure(xscrollcommand=horizontalScrollbar.set)
            horizontalScrollbar.pack(side="bottom", fill="x")

        canvas.create_window((4, 4), window=frame, anchor="nw", tags="self.canvas")

        canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

        setattr(canvas, "widget", frame)
        setattr(frame, "element", self)
        return canvas


from generalgui.app import App


