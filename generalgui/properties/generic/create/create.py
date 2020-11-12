
from generallibrary import initBases

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
        """ :param generalgui.MethodGrouper self:
            :rtype: str"""
        return self.storage["class"]

    def set_class_name(self, name):
        """ :param generalgui.MethodGrouper self:
            :param name: """
        self.storage["class"] = name
        return name

    def remove(self):
        """ Remove.

            :param generalgui.MethodGrouper self: """
        pass


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

    def all_siblings(self):
        """ Return a list of parent's children excluding self.

            :param generalgui.MethodGrouper self: """
        if self.is_app:
            return []
        else:
            children = self.get_parent().all_children().copy()
            children.remove(self)
            return children

    def next_sibling(self):
        """ Return next sibling cycling back to itself.

            :param generalgui.MethodGrouper self: """
        if self.is_app:
            return []
        else:  # Todo: This can be a lot faster if we traverse storage instead
            children = self.get_parent().all_children()
            index = children.index(self) + 1
            return children[0 if index >= len(children) else index]

    def previous_sibling(self):
        """ Return previous sibling cycling back to itself.

            :param generalgui.MethodGrouper self: """
        if self.is_app:
            return []
        else:  # Todo: This can be a lot faster if we traverse storage instead
            children = self.get_parent().all_children()
            index = children.index(self) - 1
            return children[index]



class _Create_Store:
    """ Store everything that's needed for full re-creation. """
    def __init__(self):
        self.storage = {"_instance": self}

    def save(self):
        """ Save by creating a copy of storage and removing protected.

            :param generalgui.MethodGrouper self: """
        new = self.storage.copy()

        buffer = [new]
        while buffer:
            storage = buffer[0]

            for key in [key for key in storage.keys() if key.startswith("_")]:
                del storage[key]

            if "children" in storage:
                children = [child.copy() for child in storage["children"]]
                buffer.extend(children)
                storage["children"] = children
            del buffer[0]
        return new

    def load(self, top_storage=None):
        """ Create a new tree.

            :param generalgui.MethodGrouper self:
            :param top_storage: """
        if top_storage is None:
            top_storage = self.save()

        buffer = [top_storage]
        while buffer:
            storage = buffer[0]

            storage["_instance"] = self.create_from_storage(storage)

            if "_instance" in storage:
                obj = storage["_instance"]

                # Check keys that can de-sync
                if obj.storage["class"] != obj.__class__.__name__:
                    storage["_instance"] = self.create_from_storage(storage)
                    obj.remove()
            else:
                storage["_instance"] = self.create_from_storage(storage)


            if "children" in storage:
                buffer.extend(storage["children"])
            del buffer[0]
        return top_storage["_instance"]

    def create_from_storage(self, storage):
        """ :param generalgui.MethodGrouper self:
            :param storage: """
        new = getattr(self.Generic, storage["class"])()
        storage["_instance"] = new
        new.storage = storage
        return new

@initBases
class Create(Generic, _Create_Store, _Create_Construct, _Create_Relations):
    """ Contains all methods having to do with creating a GUI part. """






























