
from generallibrary import initBases, Config

from generalgui import Generic


class _Create_Construct:
    def __init__(self, parent):
        """ :param generalgui.MethodGrouper self: """
        self._parent = self.set_parent(parent)  # Parent isn't needed for recreation
        self.set_class_name(self.__class__.__name__)

    def get_parent(self, index=0):
        """ Get this part's parent.

            :param generalgui.MethodGrouper self:
            :param index: 0 is closest and default parent. -1 top Page. """
        return self._parent if index == 0 else self.all_parents()[index]

    def set_parent(self, parent):
        """ Set this part's parent. Chained with Contain.add_child().

            :param generalgui.MethodGrouper self:
            :param generalgui.Contain or None parent: """
        if parent is None and not self.is_app:
            parent = self.App() if self.is_page else self.Page()
        self._parent = parent

        if parent:
            parent.add_child(self)

        return parent

    def get_class_name(self):
        """ :param generalgui.MethodGrouper self: """
        return self.storage["class"]

    def set_class_name(self, name):
        """ :param generalgui.MethodGrouper self: """
        self.storage["class"] = name


class _Create_Relations:
    @property
    def app(self):
        """ :param generalgui.MethodGrouper self: """
        return self if self.is_app else self.get_parent(-1).app

    def all_parents(self):
        """ Return a list of all parents.

            :param generalgui.MethodGrouper self: """
        part = self
        parents = []
        while part := part.get_parent():
            parents.append(part)
        return parents


class _Create_Store:
    """ Store everything that's needed for full re-creation. """
    def __init__(self):
        self.storage = {"_instance": self}

    def save(self):
        new = self.storage.copy()

        children = [new]
        while children:
            storage = children[0].copy()

            for key in [key for key in storage.keys() if key.startswith("_")]:
                del storage[key]

            if "children" in storage:
                children.extend(storage["children"])

            del children[0]

        return new

@initBases
class Create(Generic, _Create_Store, _Create_Construct, _Create_Relations):
    """ Contains all methods having to do with creating a GUI part. """




# All storage should happen in a seperate Config class
# Replace label.py with element.py
# Redundant and Forgiving































