
from generallibrary import TreeDiagram, hook, getBaseClassNames, SigInfo


class Generic(TreeDiagram):
    widget_cls = ...

    def __init__(self, parent):
        self.widget = None
        self.binds = []
        self._shown = True

    def __init_subclass__(cls, **kwargs):
        if cls.widget_cls is Ellipsis:
            raise AttributeError(f"widget_cls attr is not defined for {cls}")

    @property
    def shown(self):
        return self._shown

    @shown.setter
    def shown(self, shown):
        self._shown = shown

    repr_attrs = ["value", "binds", "shown"]

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
        sigInfo = SigInfo(func)
        self.binds.append(sigInfo)
        # self.binds.append(func)

    def call_binds(self):
        for sigInfo in self.binds:
            sigInfo.call()


def container_parent_check(parent):
    assert "Contain" in getBaseClassNames(parent) or parent is None

hook(Generic.set_parent, container_parent_check)

