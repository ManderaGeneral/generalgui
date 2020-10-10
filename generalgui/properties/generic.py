
import tkinter

class Generic:
    def __init__(self):
        self.is_app = self.__class__ == self.App
        self.is_page = self.__class__ == self.Page

    Page, App = ..., ...
    tk = tkinter

