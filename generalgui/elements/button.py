"""Button class that inherits Element"""

import tkinter as tk

from generallibrary.time import sleep
from generallibrary.types import strToDynamicType

from generalgui.element import Element


class Button(Element):
    """
    Controls one tkinter Button
    """
    def __init__(self, page, value, func=None, **packParameters):
        """
        Create a Button element that controls a button.

        :param Page page: Parent page
        :param str value: Text to be displayed
        :param function func: Shortcut for Button.onClick(func)
        """
        super().__init__(page)

        self.text = value
        widget = self.addWidget(tk.Button(page.getBaseWidget(), text=value), **packParameters)
        self.widgetConfig(cursor="hand2")

        self._bind("<Enter>", lambda w=widget: w.config(background="gray90"))
        self._bind("<Leave>", lambda w=widget: w.config(background="SystemButtonFace"))
        self.onClick(func)

    def click(self, animate=True):
        """
        Simple animation if button's click bind is called.
        """
        if animate:
            self._callBind("<Enter>")
            self.widget.config(relief=tk.SUNKEN)
            self.app.widget.update()
            sleep(0.05)
            self.widget.config(relief=tk.RAISED)
            self._callBind("<Leave>")
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







