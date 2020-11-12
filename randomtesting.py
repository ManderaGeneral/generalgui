"""Random testing"""

import atexit
import tkinter as tk
from generallibrary import initBases, getBaseClasses, Timer
from generalgui import Label, Page, App

from pprint import pprint




# Relation methods
# Instructions for storage values (get, set)
# Load method to replace a part's storage and iterate it to sync



# label = Label("test")
#
# label.set_class_name("Button")
#
# storage = label.app.save()
#
# new = label.load(storage)
#
# for x in (label.app, new):
#     print(x, x.get_child(), x.get_child().get_child())
#     print(id(x.storage), id(x.get_child().storage), id(x.get_child().get_child().storage))
#     print(id(x.storage["children"]), id(x.get_child().storage["children"]))




# LIB

class Test(type):
    def __init__(cls, name, bases, clsdict, *_, **__):
        if "Node" in [base.__name__ for base in bases]:
            print(name)  # HERE ** Automatically fill data_keys
        type.__init__(cls, name, bases, clsdict)


class Node(metaclass=Test):
    data_keys = []

    def __init__(self, parent=None, children_dicts=None):
        self._parent = None
        self.set_parent(parent=parent)

        self.children = []
        self.data = {}

        if children_dicts:
            for child_dict in children_dicts:
                self.load(child_dict, parent=self)

    def set_parent(self, parent):
        old_parent = self.get_parent()
        if old_parent:
            old_parent.children.remove(self)

        if parent:
            if self in parent.all_parents():
                raise AttributeError(f"Cannot set {parent} as parent for {self} as it becomes circular. ")
            parent.children.append(self)

        self._parent = parent
        return self

    def get_parent(self):
        return self._parent

    def all_parents(self):
        part = self
        parents = []
        while part := part.get_parent():
            parents.append(part)
        return parents

    def save(self):
        """ Recursively save by returning a new dictionary. """
        data = self.data.copy()
        data["children_dicts"] = [child.save() for child in self.children]
        return data

    @classmethod
    def load(cls, d, parent=None):
        return cls(parent=parent, **d)

    def copy_to(self, node):
        return self.load(d=self.save(), parent=node)

    def remove(self):
        self.set_parent(None)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.children}>"

    def __setattr__(self, key, value):
        if key in self.data_keys:
            self.data[key] = value
        object.__setattr__(self, key, value)

# USER

@initBases
class Part(Node):
    data_keys = []

    def __init__(self, class_name=None):
        if not self.data_keys:
            self.data_keys = list(locals().keys())
            self.data_keys.remove("self")


        self.class_name = class_name



part1 = Part(class_name="Parent")
part2 = Part(class_name="Middle").set_parent(part1)
part3 = Part(class_name="Bottom").set_parent(part2)

print(part1.save())
part2.remove()
print(part1.save())


# part3.set_parent(part1)
# print(part1.save())
# copied = part1.copy_to(part1)
# print(part1.save())





# print(part1.save())




# Save / Load
# part = Part(None, "Label")
# Part(part, "Button")
# Part(part, "Dropdown")
# saved = part.save()
# print(part)
# print(saved)
# part_loaded = Part.load(saved)
# print(part_loaded)
# print(part_loaded.save())

# HERE ** Nice tree concept, see if we can create another layer here and hook into it somehow


# pprint(label.app.storage)



# print(label, label.all_parents())

# print(label.get_parent().storages)

# print(label.app.store_get_dict())


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