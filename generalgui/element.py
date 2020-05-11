"""Element for generalgui, controls a widget that's not App or Page"""

import tkinter as tk
from generallibrary.types import typeChecker
from generalgui.shared_methods.element_page import Element_Page
from generalgui.shared_methods.element_page_app import Element_Page_App

class Element(Element_Page, Element_Page_App):
    """
    Element is inherited by all tkinter widgets exluding App and Page.
    Shown by default. So when it's page is shown then all of page's children are shown automatically.
    """
    def __init__(self, parentPage, widget, side="top"):
        typeChecker(parentPage, Page)

        super().__init__(parentPage, widget, side)

        self.pack()


class Text(Element):
    """Controls one tkinter Label"""
    def __init__(self, page, text):
        """
        Create a Text element that controls a label.

        :param Page page: Parent page
        :param str text: Text to be displayed
        """
        typeChecker(page, Page)

        self.text = text
        widget = tk.Label(page.widget, text=text)

        super().__init__(page, widget)

class Button(Element):
    """Controls one tkinter Button"""
    def __init__(self, page, text, lambdaFunc):
        """
        Create a Button element that controls a button.

        :param Page page: Parent page
        :param str text: Text to be displayed
        :param function lambdaFunc: Function be called when pressed
        """
        typeChecker(page, Page)

        self.text = text
        widget = tk.Button(page.widget, text=text, command=lambdaFunc)

        super().__init__(page, widget)


from generalgui.page import Page
































