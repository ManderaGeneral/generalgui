
import tkinter as tk

from generallibrary import getBaseClassNames

class Create:
    # def __init_subclass__(cls, **kwargs):
    #     obj = cls(**kwargs)
    #     assert getattr(obj, "widget_sig_info", None)
    #     return obj

    def __init__(self, parent=None):
        """ :param generalgui.MethodGrouper self: """
        self._set_parent(parent=parent)
        self.widget = None
        self.widget_sig_info = ...  # Defined by each class at bottom of hierarchy

    def _set_parent(self, parent):
        """ :param generalgui.MethodGrouper self: """
        if parent is None:
            if self.is_app:
                parent = self
            elif self.is_page:
                parent = self.App()
            else:
                parent = self.Page()
        assert "contain" in getBaseClassNames(parent)
        self.parent = parent

    def show(self):
        """ :param generalgui.MethodGrouper self: """
        # HERE ** Set parent based on current one
        self.widget = self.widget_sig_info()

    @property
    def app(self):
        """ :param generalgui.MethodGrouper self: """
        while True:
            return self if self.__class__ == self.App else self.parent.app



