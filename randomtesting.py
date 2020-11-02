"""Random testing"""

import atexit
import tkinter as tk
from generallibrary import initBases, getBaseClasses
import pickle

# from generalgui import Label
# Label("hello")



class _Contain:
    def __init__(self):
        self.children = []

class Create:
    Contain = _Contain

    args_create = ["parent"]
    args_pack = []
    args_config = []

    def __init__(self, parent):
        self.parent = self.set_parent(parent)

    def __repr__(self):
        return self.__class__.__name__

    def set_parent(self, parent):
        if parent is None and self.__class__ != Page:
            parent = Page()

        self.parent = parent
        return parent



class App:
    pass


@initBases
class Page(Create, Create.Contain):
    def __init__(self, parent=None):
        pass

@initBases
class Label(Create):
    args_config = Create.args_config + ["value"]

    def __init__(self, value=None, parent=None):
        self.value = value


label = Label("hello")


print(label, label.parent, label.parent.parent)  # HERE ** Start like this! Don't bother with tkinter yet








# HERE ** Plan was to store all args as attributes. BUT: they should be protected. I dont want to make a property for each attribute.
# WANT: Easy autocompletion for each arg
# WANT: Ability to configure multiple
# WANT: Automatic updating when changing a value
# WANT: Allowing adding to args lower in hierarchy (i.e. value for Label)

# DONT: Update after changing one of multiple values, only once
# DONT: Rely on manual updating as it's prone for de-sync issues

# IDEA: Remove config method, make them all attributes,
# IDEA: Convert old Styler to a config class for generallibrary, use that here
# Give combined lists to Config class, then add code for our purpose




# Create_Construct
    # @deco_group_top
    # def get_shown(self, propagate=True):
    #     """ Get whether this part and all its parents aren't is_hidden.
    #
    #         :param generalgui.MethodGrouper self:
    #         :param propagate: """
    #     if not propagate:
    #         return self._shown
    #
    #     for part in self.parents(include_self=True):
    #         if not part.get_shown(propagate=False):
    #             return False
    #     return True
    #
    # @deco_group_top
    # def set_shown(self, shown):
    #     """ Show this part.
    #         If this part doesn't have a widget then it's created.
    #         If widget is hidden then it's re-packed.
    #
    #
    #         :param generalgui.MethodGrouper self:
    #         :param shown: """
    #     if shown:
    #         self._shown = False
    #         if self.destroy_when_hidden:
    #             return self.remove()
    #         else:
    #             self.widget.hide()
    #     else:
    #         pass
    #
    # @deco_group_top
    # def get_removed(self):
    #     """ Remove this part from it's parent's children and destroys widget.
    #
    #         :param generalgui.MethodGrouper self: """
    #
    # @deco_group_top
    # def set_removed(self):
    #     """ Remove this part from it's parent's children and destroys widget.
    #
    #         :param generalgui.MethodGrouper self: """
    #     if self.parent():
    #         self.parent().children.remove(self)
    #
    #     self._parent = None
    #     self._destroy()