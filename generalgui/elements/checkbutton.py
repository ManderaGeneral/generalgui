
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

    # Editable
    _editable_tk_var = tk.BooleanVar
    def _editable_hook_get(self):
        return self.toggled()
    def _editable_hook_set(self):
        self._toggled = self._editable_tk_var_inst.get()  # Set without triggering draw

    # Toggle
    def _draw_toggle_hook(self):
        self._editable_tk_var_inst.set(self.toggled())

    def __init__(self, parent=None, text=None, toggled=None):
        pass


