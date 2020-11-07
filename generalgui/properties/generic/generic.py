
import tkinter


class Generic:
    Create = ...

    App = ...
    Page = ...
    Label = ...

    tk = tkinter

    def __init__(self):
        cls = self.__class__
        self.is_app = cls is self.App
        self.is_page = cls is self.Page
