
import tkinter as tk

from generalgui.properties.generic import Generic
from generalgui.properties.value import Value


class Label(Generic, Value):
    widget = ... # type: tk.Label
    widget_cls = tk.Label

    def __init__(self, parent=None, value=None):
        pass
