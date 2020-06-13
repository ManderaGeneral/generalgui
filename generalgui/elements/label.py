"""Label class that inherits Element"""

import tkinter as tk

from generalgui.element import Element

from generallibrary.types import strToDynamicType


class Label(Element):
    """Controls one tkinter Label"""
    def __init__(self, parentPage, value=None, **parameters):
        """
        Create a Label element that controls a label.

        :param generalgui.Page parentPage: Parent page
        :param str value: Text to be displayed
        :param parameters: Both config and pack parameters together
        """
        super().__init__(parentPage, tk.Label, text=value, **parameters)

    def setValue(self, value):
        """
        Set value of label

        :param any value: Any value, is cast to str
        """
        if value is None:
            value = ""
        self.widget["text"] = str(value)

    def getValue(self):
        """
        Get value of label as a dynamic type, "tRue" becomes True for example
        """
        return strToDynamicType(self.widget["text"])
