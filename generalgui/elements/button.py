"""Button class that inherits Element"""

import tkinter as tk

from generallibrary.types import strToDynamicType
from generallibrary.functions import defaults

from generalgui import Label


class Button(Label):
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
        super().__init__(parentPage, value=value, onClick=onClick, **defaults(parameters, relief="raised", padx=5, pady=5))







