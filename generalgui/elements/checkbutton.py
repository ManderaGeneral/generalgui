"""Checkbutton class that inherits Element"""

import tkinter as tk

from generalgui.element import Element


class Checkbutton(Element):
    """
    Controls one tkinter Checkbutton
    """
    def __init__(self, page, default=False, **packParameters):
        """
        Create an Entry element that controls an entry.

        :param generalgui.Page page: Parent page
        :param bool default: Whether to be created on or off
        """
        super().__init__(page)

        self.default = default
        self._boolVar = tk.BooleanVar(value=default)
        self.addWidget(tk.Checkbutton(page.getBaseWidget(), variable=self._boolVar), **packParameters)

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
