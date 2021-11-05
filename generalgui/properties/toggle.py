
import tkinter as tk


class Toggle:
    """ Use methods instead of property so that it's easy to change it with hooks. """
    def __init__(self, toggled=None):
        """ :param generalgui.MethodGrouper self:
            :param toggled: """
        self._toggled = bool(toggled)
        # self.bind(self._sync_tk_to_toggle)
        self._boolVar = ...

    def draw_create_hook(self, kwargs):
        self._boolVar = tk.BooleanVar()
        self._boolVar.trace_add("write", lambda *_: self._sync_tk_to_toggle())
        self._sync_toggle_to_tk()
        kwargs["variable"] = self._boolVar
        return kwargs
        # super().__init__(parentPage, tk.Checkbutton, variable=self._boolVar, cursor="hand2", **parameters)

    def _sync_tk_to_toggle(self):
        self._toggled = self._boolVar.get()

    def _sync_toggle_to_tk(self):
        if self._boolVar is not Ellipsis:
            self._boolVar.set(self.toggled())

    def toggled(self):
        return self._toggled

    def toggle(self, bool_=None):
        if bool_ is None:
            bool_ = not self._toggled
        self._toggled = bool_
        self._sync_toggle_to_tk()



