
import tkinter as tk

from generalgui.properties.generic import Generic
from generalgui.properties.text import Text


class Label(Generic, Text):
    widget = ... # type: tk.Label
    widget_cls = tk.Label

    def __init__(self, parent=None, text=None):
        pass
