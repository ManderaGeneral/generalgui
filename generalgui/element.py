
import tkinter as tk
from generallibrary.types import typeChecker


class Element:
    def __init__(self, parentPage, widget):
        typeChecker(parentPage, Page)

        self.parentPage = parentPage
        self.widget = widget

        widget.pack()

class Text(Element):
    def __init__(self, parentPage, text):
        typeChecker(parentPage, Page)

        self.text = text
        super().__init__(parentPage, tk.Label(parentPage.widget, text=text))


from generalgui.page import Page
