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

        super().__init__(parentPage=parentPage)

        if height is None and width is None:
            self.addWidget(tk.Frame(parentPage.getBaseWidget()), **packParameters)
        else:
            self._getScrollableWidget(parentPage, width, height, vsb, hsb, **packParameters)

    def _getScrollableWidget(self, parentPage, width, height, vsb, hsb, **packParameters):
        canvas = tk.Canvas(parentPage.getBaseWidget(), width=width, height=height)
        self.addWidget(canvas, **packParameters)
        canvas.pack_propagate(0)

        frame = tk.Frame(canvas, bg="green")
        self.addWidget(frame, makeBase=True, pack=False)

        if vsb:
            verticalScrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
            canvas.configure(yscrollcommand=verticalScrollbar.set)
            verticalScrollbar.pack(side="right", fill="y")

        if hsb:
            horizontalScrollbar = tk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
            canvas.configure(xscrollcommand=horizontalScrollbar.set)
            horizontalScrollbar.pack(side="bottom", fill="x")

        windowId = canvas.create_window(0, 0, window=frame, anchor="nw")

        def _canvasConfigure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfig(windowId, width=event.width)
        canvas.bind("<Configure>", _canvasConfigure)

        return canvas



from generalgui.app import App











































