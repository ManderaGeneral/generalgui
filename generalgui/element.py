
from tkinter import Label

class Element:
    def __init__(self, widget):
        self.widget = widget
        widget.pack()

class Text(Element):
    def __init__(self, page, text):
        self.text = text

        super().__init__(Label(page.frame, text=text))

