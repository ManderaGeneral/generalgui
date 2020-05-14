"""Button class that inherits Element"""

import tkinter as tk

from generallibrary.time import sleep

from generalgui.element import Element


class Button(Element):
    """
    Controls one tkinter Button
    """
    def __init__(self, page, text, func=None, **packParameters):
        """
        Create a Button element that controls a button.

        :param Page page: Parent page
        :param str text: Text to be displayed
        :param function func: Shortcut for Button.onClick(func)
        """
        self.text = text
        widget = tk.Button(page.getBaseWidget(), text=text)
        widget.config(cursor='hand2')

        super().__init__(page, widget, **packParameters)

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





