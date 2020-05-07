
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
        widget = tk.Label(parentPage.widget, text=text)

        super().__init__(parentPage, widget)

class Button(Element):
    def __init__(self, parentPage, text, lambdaFunc):
        typeChecker(parentPage, Page)

        self.text = text
        widget = tk.Button(parentPage.widget, text=text, command=lambdaFunc)

        super().__init__(parentPage, widget)


from generalgui.page import Page
