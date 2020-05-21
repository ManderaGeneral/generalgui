"""Button class that inherits Element"""

import tkinter as tk

from generallibrary.time import sleep
from generallibrary.types import strToDynamicType

from generalgui.element import Element


class Button(Element):
    """
    Controls one tkinter Button
    """
    def __init__(self, parentPage, value, func=None, **parameters):
        """
        Create a Button element that controls a button.

        :param generalgui.Page parentPage: Parent page
        :param str value: Text to be displayed
        :param function func: Shortcut for Button.onClick(func)
        """
        super().__init__(parentPage, tk.Button, text=value, cursor="hand2", **parameters)


        self.createStyle(name="Hover", hook="<Enter>", unhook="<Leave>", bg="gray90")
        self.onClick(func)

    def click(self, animate=True):
        """
        Simple animation if button's click bind is called.
        """
        # HERE ** Turn this into a style instead, so create a method to copy and extend a style?
        if animate:
            self.styleHandler.enable("Hover")
            self.widget.config(relief=tk.SUNKEN)
            self.app.widget.update()
            sleep(0.05)
            self.widget.config(relief=tk.RAISED)
            self.styleHandler.disable("Hover")
        return super().click()

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







