"""Scrollbar class that inherits Element"""

import tkinter as tk

from generalgui.element import Element


class Scrollbar(Element):
    """
    Controls one tkinter Scrollbar
    """
    def __init__(self, parentPage, **parameters):
        """
        Create a Scrollbar element that controls a scrollbar.

        :param generalgui.Page parentPage: Parent page
        """
        super().__init__(parentPage, tk.Scrollbar, **parameters)








