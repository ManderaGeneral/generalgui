import tkinter as tk

from generalgui.properties.generic import Generic
from generalgui.properties.text import Text
from generalgui.properties.toggle import Toggle
from generalgui.properties.editable import Editable


class Checkbutton(Generic, Text, Toggle, Editable):
    # Type hinting
    widget = ...  # type: tk.Checkbutton

    # Generic
    widget_cls = tk.Checkbutton
    widget_var = tk.BooleanVar  # HERE ** Maybe we can define vars here? Decouple Editable from Toggle

    # Editable
    editable_attr = "_toggle"

    def __init__(self, parent=None, text=None, toggled=None,):
        pass


