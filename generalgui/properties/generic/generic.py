
import tkinter
from generallibrary import getBaseClasses, SigInfo, HierarchyStorer


class Generic(metaclass=HierarchyStorer, base="Generic"):
    Create, Contain, Value, App, Page, Label = ..., ..., ..., ..., ..., ...

    tk = tkinter

    def __init__(self):
        cls = self.__class__
        self.is_app = cls is self.App
        self.is_page = cls is self.Page
