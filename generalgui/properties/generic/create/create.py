
from generallibrary import initBases, Config

from generalgui import Generic


class _Create_Construct:
    def __init__(self, parent):
        """ :param generalgui.MethodGrouper self: """
        self._parent = self.set_parent(parent)

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
    def __init__(self):
        self.storages = []
        self.store_add("class", lambda x=self: x.__class__.__name__)

    def store_add(self, name, getter, setter=None):
        """ :param generalgui.MethodGrouper self: """
        self.storages.append(Storage(name=name, getter=getter, setter=setter))

    def store_get_dict(self):
        """ :param generalgui.MethodGrouper self: """
        return {storage.name: storage.getter() for storage in self.storages}


@initBases
class Create(Generic, _Create_Construct, _Create_Relations, _Create_Store):
    """ Contains all methods having to do with creating a GUI part. """


class Storage:
    def __init__(self, name, getter, setter):
        self.name = name
        self.getter = getter
        self.setter = setter



# All storage should happen in a seperate Config class
# Replace label.py with element.py
# Redundant and Forgiving































