
from generallibrary import TreeDiagram, hook, getBaseClassNames, SigInfo

from generalgui import Draw


class Binder:
    def __init__(self):
        self.binds = []

    def bind(self, func):
        sigInfo = SigInfo(func)
        self.binds.append(sigInfo)
        # self.binds.append(func)

    def call_binds(self):
        return tuple(sigInfo.call() for sigInfo in self.binds)



class Generic(TreeDiagram, Binder):
    widget_cls = ...
    id = 0

    def __init__(self, parent):
        self.widget = None
        self.binds = []
        self._shown = True
        self.assign_id()

    def __getstate__(self):  # For pickle
        self.widget = None
        # self._parents = []
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__ = state
        self.assign_id()

    def assign_id(self):
        self.id = Generic.id
        Generic.id += 1

    def __init_subclass__(cls, **kwargs):
        if cls.widget_cls is Ellipsis:
            raise AttributeError(f"widget_cls attr is not defined for {cls}")

    repr_attrs = ["id", "value", "binds", "shown"]
    def __repr__(self):
        parts = [
            self.__class__.__name__,
        ]

        attr_dict = {key: getattr(self, key) for key in self.repr_attrs if getattr(self, key, None)}
        if attr_dict:
            parts.append(str(attr_dict))

        return f"<GUI {', '.join(parts)}>"

    def __eq__(self, other):
        return repr(self) == repr(other)  # might be slow

    def __hash__(self):
        return super().__hash__()

    def draw(self):
        return Draw(self)

    def copy_part(self, parent=None):
        old_parent, old_index = self.get_parent(), self.get_index()
        self.set_parent(parent=None)

        new = self.copy_node()
        new.set_parent(parent=parent)

        self.set_parent(parent=old_parent)
        self.set_index(index=old_index)

        if parent is None:
            new.draw()

        # widget = self.widget
        # old_parent = self.get_parent()
        #
        # self.set_parent(None)
        # self.widget = None
        #
        # new = self.copy_node()
        #
        # self.widget = widget
        # self.set_parent(parent=old_parent)
        #
        # for child in new.get_children(depth=-1, gen=True):
        #     child.widget = None
        # new.set_parent(parent=parent)
        # if parent is None:
        #     new.draw()

    @property
    def shown(self):
        return self._shown

    @shown.setter
    def shown(self, shown):
        self._shown = shown

    def is_hidden_by_parent(self):
        for parent in self.get_parents(depth=-1, gen=True):
            if parent and not parent.shown:
                return True
        return False

    def is_app(self):
        return self.__class__.__name__ == "App"

    def is_page(self):
        return self.__class__.__name__ == "Page"


def container_parent_check(parent):
    assert "Contain" in getBaseClassNames(parent) or parent is None

hook(Generic.set_parent, container_parent_check)

