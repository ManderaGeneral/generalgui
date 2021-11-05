
import tkinter as tk

from generalgui.properties.generic import Generic
from generalgui.properties.text import Text


class Label(Generic, Text):
    widget_cls = tk.Entry
    widget = ...  # type: tk.Entry

    def __init__(self, parent=None, value=None):
        pass
