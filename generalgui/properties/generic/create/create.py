
from generallibrary import initBases

from generalgui import Generic


class _Create_Construct:
    def __init__(self, parent):
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
        self._parent = parent

        if parent is None and not self.is_page:
            parent = self.Page()

        if parent is not None:
            parent.add_child(self)

        return parent


class _Create_Relations:
    pass


class _Create_Store:
    pass


@initBases
class Create(Generic, _Create_Construct, _Create_Relations, _Create_Store):
    """ Contains all methods having to do with creating a GUI part. """





































