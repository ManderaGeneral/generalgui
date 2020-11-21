
from generallibrary import HierarchyStorer, attributes, addToDictInDict

import atexit


class _Generic(metaclass=HierarchyStorer, base="_Generic"):
    _Generic, _Create, _Contain, _Value, App, Page, Label = ..., ..., ..., ..., ..., ..., ...  # Wet for autocompletion
    _cartridge = None
    _atexit_funcs = []
    def __init__(self):
        if self.get_cartridge() is None:
            self.__class__.set_cartridge("tkinter")

    @classmethod
    def _atexit(cls):
        for func in cls._atexit_funcs:
            func()

    @classmethod
    def get_cartridge(cls):
        return cls._Generic._cartridge

    @classmethod
    def set_cartridge(cls, cartridge):
        cls._Generic._cartridge = cartridge
        if cartridge == "tkinter":
            import generalgui.cartridge.tkinter
            cls._load_cartridge(generalgui.cartridge.tkinter)
        else:
            raise AttributeError(f"No such cartridge: '{cartridge}'")

    @classmethod
    def _load_cartridge(cls, pkg):
        """ Load tkinter hooks into parts and Tree diagram.
            Todo: Keep track of overriden hooks to be able to withdraw cartridge.
                Possibly wrap methods for stacking. Thinking about __init__ for example.
                Since initBases actually ignores overriden inits it should be possible.
            Todo: Make cartridge general and put it in library, maybe use dynamic imports.
            Todo: Cannot use attributes as we need it to replace __init__ too. """
        cls.original_methods = {}  # HERE ** do something like this, use attributes_defined_by from lib
        dir_pkg = dir(pkg)
        for part_cls in getattr(cls, "_inheriters"):
            if part_cls.__name__ in dir_pkg:
                hook_cls = getattr(pkg, part_cls.__name__)
                for attr_name in attributes(hook_cls):
                    addToDictInDict(cls.original_methods, part_cls.__name__, **{attr_name: getattr(part_cls, attr_name)})
                    setattr(part_cls, attr_name, getattr(hook_cls, attr_name))

    def is_app(self):
        return self.__class__ is self.App

    def is_page(self):
        return self.__class__ is self.Page

    def __repr__(self):
        return f"<GUI {self.__class__.__name__}>"

atexit.unregister(_Generic._atexit)
atexit.register(_Generic._atexit)
