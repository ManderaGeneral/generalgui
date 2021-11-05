
import tkinter as tk


class Editable:
    """ Property to easily allow automatic two way sync between Part and tkinter. """
    editable_attr = ...  # Attribute key (_toggled or _text presumably) which can be read and changed directly when syncing

    def __init__(self):
        """ :param generalgui.MethodGrouper self: """
        self._boolVar = ...

    def draw_create_hook(self, kwargs):
        self._boolVar = tk.BooleanVar()
        self._sync_toggle_to_tk()
        kwargs["variable"] = self._boolVar
        return kwargs

    def _sync_tk_to_toggle(self):
        self._toggled = not self._boolVar.get()  # Invert because of bind order...

    def _sync_toggle_to_tk(self):
        self._boolVar.set(self.toggled())

    def toggled(self):
        return self._toggled

    def toggle(self, bool_=None):
        if bool_ is None:
            bool_ = not self._toggled
        self._toggled = bool_
        self._sync_toggle_to_tk()



