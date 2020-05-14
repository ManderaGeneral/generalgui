"""Label class that inherits Element"""

import tkinter as tk

from generalgui.element import Element


class Label(Element):
    """Controls one tkinter Label"""
    def __init__(self, page, text):
        """
        Create a Label element that controls a label.

        :param Page page: Parent page
        :param str text: Text to be displayed
        """
        self.text = text
        widget = tk.Label(page.getBaseWidget(), text=text)

        super().__init__(page, widget)

