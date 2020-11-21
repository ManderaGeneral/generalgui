
from generallibrary import initBases, TreeDiagram

from generalgui import _Generic


@initBases
class _Create(TreeDiagram, _Generic):
    """ Contains all methods having to do with creating a GUI part. """
    def __init__(self, parent=None, bgcolor=None):
        self.bgcolor = self.data_keys_add("bgcolor", bgcolor)

        if parent is None and not self.is_app():
            parent = self.App() if self.is_page() else self.Page()

        if parent and self.get_parent() != parent:
            self.set_parent(parent=parent)

    def hook_draw(self): pass

    def draw(self):
        self.hook_draw()

    def app(self):
        """ :param generalgui.MethodGrouper self: """
        return self if self.is_app() else self.get_parent(-1)

    def hook_add_child(self, child):
        raise AttributeError(f"'{self}' hasn't inherited Container.")





























