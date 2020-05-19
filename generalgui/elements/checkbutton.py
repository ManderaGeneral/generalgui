"""Checkbutton class that inherits Element"""

import tkinter as tk

from generalgui.element import Element


class Checkbutton(Element):
    """
    Controls one tkinter Checkbutton
    """
    def __init__(self, parentPage, default=False, **parameters):
        """
        Create an Entry element that controls an entry.

        :param generalgui.Page parentPage: Parent page
        :param bool default: Whether to be created on or off
        :param parameters: Both config and pack parameters together
        """
        self._boolVar = tk.BooleanVar(value=default)
        super().__init__(parentPage, tk.Checkbutton, variable=self._boolVar, **parameters)
        self.default = default

    def toggle(self):
        """
        Turn on checkbutton if it's off and vice versa.
        """
        self.setValue(not self.getValue())

    def getValue(self):
        """
        Get whether checkbutton is toggled or not.
        """
        return self._boolVar.get()

    def setValue(self, value):
        """
        Set the value of checkbutton

        :param bool value: New boolean value
        """
        self._boolVar.set(value)
