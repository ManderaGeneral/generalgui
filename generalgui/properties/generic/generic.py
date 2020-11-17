
from generallibrary import HierarchyStorer, attributes

class Generic(metaclass=HierarchyStorer, base="Generic"):
    Generic, Create, Contain, Value, App, Page, Label = ..., ..., ..., ..., ..., ..., ...  # Wet for autocompletion

    _cartridge = None
    def __init__(self):
        if self.get_cartridge() is None:

            self.__class__.set_cartridge("tkinter")

    @classmethod
    def get_cartridge(cls):
        return cls.Generic._cartridge

    @classmethod
    def set_cartridge(cls, cartridge):
        cls.Generic._cartridge = cartridge
        if cartridge == "tkinter":
            import generalgui.cartridge.tkinter
            cls._load_cartridge(generalgui.cartridge.tkinter)
        else:
            raise AttributeError(f"No such cartridge: '{cartridge}'")

    @classmethod
    def _load_cartridge(cls, pkg):
        """ Load tkinter hooks into parts and Tree diagram.
            Todo: Keep track of overriden hooks to be able to withdraw cartridge.
            Todo: Possibly wrap methods for stacking. Thinking about __init__ for example. """
        dir_pkg = dir(pkg)
        for part_cls in getattr(cls, "_inheriters"):
            if part_cls.__name__ in dir_pkg:
                hook_cls = getattr(pkg, part_cls.__name__)
                for hook_name in attributes(hook_cls):
                    setattr(part_cls, hook_name, getattr(hook_cls, hook_name))

    def is_app(self):
        return self.__class__ is self.App

    def is_page(self):
        return self.__class__ is self.Page

    def __repr__(self):
        return f"<GUI {self.__class__.__name__}>"
