
import tkinter as tk
from generallibrary.types import typeChecker
from generalgui.shared_methods import Element_Page, Element_Page_App

class Element(Element_Page, Element_Page_App):
    def __init__(self, page, widget, side="top"):
        typeChecker(page, Page)

        self.page = page
        self.widget = widget
        self.side = side

        setattr(widget, "element", self)
        self.pack()

class Text(Element):
    def __init__(self, page, text):
        typeChecker(page, Page)

        self.text = text
        widget = tk.Label(page.widget, text=text)

        super().__init__(page, widget)

class Button(Element):
    def __init__(self, page, text, lambdaFunc):
        typeChecker(page, Page)

        self.text = text
        widget = tk.Button(page.widget, text=text, command=lambdaFunc)

        super().__init__(page, widget)


from generalgui.page import Page
