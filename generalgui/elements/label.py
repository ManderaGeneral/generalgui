"""Label class that inherits Element"""

import tkinter as tk

from generalgui.element import Element


class Label(Element):
    """Controls one tkinter Label"""
    def __init__(self, page, value, **packParameters):
        """
        Create a Label element that controls a label.

        :param Page page: Parent page
        :param str value: Text to be displayed
        """
        super().__init__(page)

        self.addWidget(tk.Label(page.getBaseWidget(), text=value), **packParameters)

    def setValue(self, value):
        if value is None:
            value = ""
        self.widget["text"] = str(value)

    def getValue(self):
        return self.widget["text"]
