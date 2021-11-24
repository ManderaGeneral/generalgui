
import tkinter as tk

from generalgui.properties.generic import Generic
from generalgui.properties.text import Text
from generalgui.properties.toggle import Toggle
from generalgui.properties.editable import Editable


class Entry(Generic, Text, Toggle, Editable):
    # Type hinting
    widget = ...  # type: tk.Entry

    # Generic
    widget_cls = tk.Entry

    # Editable
    _editable_tk_var = tk.StringVar
    def _editable_hook_get(self):
        return self.text
    def _editable_hook_set(self):
        self.text = self._editable_tk_var_inst.get()

    def __init__(self, parent=None, text=None):
        pass


