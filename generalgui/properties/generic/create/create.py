
from generallibrary import initBases, TreeDiagram

from generalgui import Generic



@initBases
class Create(TreeDiagram, Generic):
    """ Contains all methods having to do with creating a GUI part. """
    def __init__(self, parent=None):
        self.hook_add_child = self._disable_add_child

        if parent is None and not self.is_app():
            parent = self.App() if self.is_page() else self.Page()
        self.set_parent(parent=parent)

    def _disable_add_child(self, child):
        raise AttributeError(f"'{self}' hasn't inherited Container.")

    def app(self):
        """ :param generalgui.MethodGrouper self: """
        return self if self.is_app() else self.get_parent(-1)





























