"""Label class that inherits Element"""

import tkinter as tk

from generalgui.element import Element


class Label(Element):
    """Controls one tkinter Label"""
    def __init__(self, parentPage, value, **parameters):
        """
        Create a Label element that controls a label.

        :param generalgui.Page parentPage: Parent page
        :param str value: Text to be displayed
        :param parameters: Both config and pack parameters together
        """
        super().__init__(parentPage, tk.Label, text=value, **parameters)

    def setValue(self, value):
        if value is None:
            value = ""
        self.widget["text"] = str(value)

    def getValue(self):
        return self.widget["text"]
