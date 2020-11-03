
from generallibrary import initBases

from generalgui import Generic


class _Create_Construct:
    def __init__(self, parent=None):
        """ :param generalgui.MethodGrouper self: """
        self._parent = self.set_parent(parent)

    def get_parent(self):
        """ Get this part's parent.

            :param generalgui.MethodGrouper self: """
        return self._parent

    def set_parent(self, parent):
        """ Set this part's parent.

            :param generalgui.MethodGrouper self:
            :param generalgui.MethodGrouper parent: """
        if parent is None and self.__class__ != self.Page:
            parent = self.Page()

        self._parent = parent
        return parent


class _Create_Relations:
    pass


class _Create_Store:
    pass


@initBases
class Create(Generic, _Create_Construct, _Create_Relations, _Create_Store):
    """ Contains all methods having to do with creating a GUI part. """
    Contain = ...
    Value = ...

Generic.Create = Create





































