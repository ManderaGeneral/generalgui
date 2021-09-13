
from generallibrary import TreeDiagram, hook, getBaseClassNames


class Generic(TreeDiagram):
    def __init__(self, parent):
        self.binds = []
        self._shown = True

    @property
    def shown(self):
        return self._shown

    @property
    def hidden(self):
        return not self.shown

    def show(self):
        pass

    def hide(self):
        pass

    repr_attrs = ["value", "binds"]

    def __repr__(self):
        parts = [self.__class__.__name__]

        attr_dict = {key: getattr(self, key) for key in self.repr_attrs if getattr(self, key, None)}
        if attr_dict:
            parts.append(str(attr_dict))

        return f"<GUI {', '.join(parts)}>"

    def is_app(self):
        return self.__class__.__name__ == "App"

    def is_page(self):
        return self.__class__.__name__ == "Page"

    def bind(self, func):
        self.binds.append(func)


def container_parent_check(parent):
    assert "Contain" in getBaseClassNames(parent)

hook(Generic.set_parent, container_parent_check)

