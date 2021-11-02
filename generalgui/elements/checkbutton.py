import tkinter as tk

from generalgui.properties.generic import Generic
from generalgui.properties.value import Value
from generalgui.properties.toggle import Toggle


class Checkbutton(Generic, Value, Toggle):
    widget = ...  # type: tk.Checkbutton
    widget_cls = tk.Checkbutton

    def __init__(self, parent=None, value=None, toggled=None,):
        pass


