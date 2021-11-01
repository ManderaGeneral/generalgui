
import tkinter as tk


class Toggle:
    """ Use methods instead of property so that it's easy to change it with hooks. """
    def __init__(self, toggled):
        """ :param generalgui.MethodGrouper self:
            :param toggled: """
        self._toggled = bool(toggled)
        self.bind(self._sync_toggle)
        self._boolVar = ...

    def draw_create_hook(self, kwargs):
        self._boolVar = tk.BooleanVar(value=self.toggled())
        kwargs["variable"] = self._boolVar
        return kwargs
        # super().__init__(parentPage, tk.Checkbutton, variable=self._boolVar, cursor="hand2", **parameters)

    def _sync_toggle(self):
        self.toggle(self._boolVar.get())
        # print(self.toggled())

    def toggled(self):
        return self._toggled

    def toggle(self, bool_=None):
        if bool is None:
            self._toggled = not self._toggled
        else:
            self._toggled = bool_

    def toggle_on(self):
        self._toggled = True

    def toggle_off(self):
        self._toggled = False



