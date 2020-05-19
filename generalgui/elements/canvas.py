"""Canvas class that inherits Element"""

import tkinter as tk

from generalgui.element import Element


class Canvas(Element):
    """
    Controls one tkinter Frame

    Attributes:
        widget  Hello
    """
    def __init__(self, parentPage, **parameters):
        """
        Create a Canvas element that controls a canvas.

        :param generalgui.Page parentPage: Parent page
        """
        super().__init__(parentPage, tk.Canvas, **parameters)








