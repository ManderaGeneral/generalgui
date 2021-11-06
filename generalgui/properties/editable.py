

# def trace(cls, attr, func):
#     # Already traced, should probably allow stacking
#     # Todo: Move trace to generallibrary.
#     if cls.__setattr__ is not object.__setattr__:
#         return
#
#     def deco(self, name, value):
#         object.__setattr__(self, name, value)
#         if name == attr:
#             func()
#     cls.__setattr__ = deco


class Editable:
    """ Property to easily allow tk to update Part attrs when changed by using tk var trace. """
    # I think only Editable parts should need a tk var
    _editable_tk_var = ...
    _editable_tk_var_inst = ...

    def _editable_hook_get(self):
        """ Hook to get Part's attribute. """

    def _editable_hook_set(self):
        """ Hook to update Part's attribute when tk is edited. """

    def __init__(self):
        """ :param generalgui.MethodGrouper self: """
        assert self._editable_tk_var is not Ellipsis
        assert self._editable_hook_get is not Editable._editable_hook_get
        assert self._editable_hook_set is not Editable._editable_hook_set

    def draw_create_hook(self, kwargs):
        self._editable_tk_var_inst = self._editable_tk_var()
        self._editable_tk_var_inst.trace_add("write", lambda *_: self._editable_hook_set())
        self._editable_tk_var_inst.set(self._editable_hook_get())  # Set value once, then we let whatever other method handles it call draw

        key = "variable" if self._editable_tk_var.__name__ == "BooleanVar" else "textvariable"

        kwargs[key] = self._editable_tk_var_inst
        return kwargs




