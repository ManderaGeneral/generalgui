"""Frame class that inherits Element"""

import tkinter as tk

from generalgui.element import Element


class Frame(Element):
    """
    Controls one tkinter Frame
    """
    def __init__(self, parentPage, **parameters):
        """
        Create a Frame element that controls a frame.

        :param generalgui.Page parentPage: Parent page
        """
        super().__init__(parentPage, tk.Frame, **parameters)



