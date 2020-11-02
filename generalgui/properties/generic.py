
import tkinter
from generalgui.properties.create import _Create


class Generic:
    Create = _Create
    def __init__(self):
        self.is_app = self.__class__ == self.App
        self.is_page = self.__class__ == self.Page

    Page, App = ..., ...
    tk = tkinter

