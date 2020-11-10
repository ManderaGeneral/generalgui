
import tkinter


class Watcher(type):
    def __init__(cls, name, bases, clsdict):
        if len(cls.mro()) > 2:
            print("was subclassed by " + name)  # HERE ** Automatically store subclasses
        super(Watcher, cls).__init__(name, bases, clsdict)


class Generic(metaclass=Watcher):
    create = ...
    contain = ...
    value = ...

    app = ...
    page = ...
    label = ...

    tk = tkinter

    def __init__(self):
        cls = self.__class__
        self.is_app = cls is self.app
        self.is_page = cls is self.page
