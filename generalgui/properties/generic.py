
from generallibrary import TreeDiagram, hook

from generalgui.properties.funcs import set_parent_hook
from generalgui.properties.generic_app import App
from generalgui.properties.generic_binder import Binder
from generalgui.properties.generic_drawer import Drawer
from generalgui.properties.generic_indexer import Indexer
from generalgui.properties.generic_states import States

from generalvector import Vec


class Generic(TreeDiagram, States, Binder, Indexer, Drawer, App):
    """ Used for every part. """
    widget_cls = ...

    def __init__(self, parent, /, **extra):
        pass

    def __getstate__(self):  # For pickle
        # self.widget = None
        # self._parents = []
        dict_ = self.__dict__.copy()
        dict_["widget"] = None
        return dict_

    def __setstate__(self, state):
        self.__dict__ = state
        self.id_assign()

    def __init_subclass__(cls, **kwargs):
        if cls.widget_cls is Ellipsis:
            raise AttributeError(f"widget_cls attr is not defined for {cls}")

    repr_attrs = ("id", "text", "binds", "shown", "exists")
    def __repr__(self):
        parts = [
            self.__class__.__name__,
        ]
        attr_dict = {key: getattr(self, key) for key in self.repr_attrs if getattr(self, key, ...) is not ...}
        if attr_dict:
            parts.append(str(attr_dict))

        return f"<GUI {', '.join(parts)}>"

    def copy_part(self, parent=None):
        old_parent, old_index = self.get_parent(), self.get_index()
        self.set_parent(parent=None)

        new = self.copy_node()
        new.set_parent(parent=parent)

        self.set_parent(parent=old_parent)
        self.set_index(index=old_index)
        # from pprint import pprint
        # pprint(Generic.orders)

    def rainbow(self):
        for part in self.get_all(gen=True):  # type: Generic
            part.widget.config(bg=Vec.random(50, 255).hex())


Drawer.register_mainloop()
hook(Generic.set_parent, set_parent_hook, owner=Generic)

