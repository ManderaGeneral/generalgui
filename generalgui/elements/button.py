"""Button class that inherits Element"""

import tkinter as tk

from generallibrary.types import strToDynamicType
from generallibrary.functions import defaults

from generalgui.element import Element


class Button(Element):
    """
    Controls one tkinter Button
    """
    def __init__(self, parentPage, value, onClick=None, **parameters):
        """
        Create a Button element that controls a button.

        :param generalgui.Page parentPage: Parent page
        :param str value: Text to be displayed
        :param function func: Shortcut for Button.onClick(func)
        """
        super().__init__(parentPage, tk.Label, text=value, onClick=onClick, **defaults(parameters, relief="raised", padx=5, pady=5))

        # self.setBindPropagation("<Button-1>", False)

    def setValue(self, value):
        """
        Set the value (text) of the button.

        :param str or float or bool or None value:
        """
        self.widget["text"] = str(value)

    def getValue(self):
        """
        Get the value (text) of the button as a dynamic type.
        """
        return strToDynamicType(self.widget["text"])







