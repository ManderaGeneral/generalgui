
from generallibrary import HierarchyStorer


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
            from generalgui.cartridge.tkinter.tkinter import load_cartridge
            load_cartridge(Generic)
        else:
            raise AttributeError(f"No such cartridge: '{cartridge}'")



    def is_app(self):
        return self.__class__ is self.App

    def is_page(self):
        return self.__class__ is self.Page

    def __repr__(self):
        return f"<GUI {self.__class__.__name__}>"
