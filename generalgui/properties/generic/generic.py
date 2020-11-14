
from generallibrary import HierarchyStorer


class Generic(metaclass=HierarchyStorer, base="Generic"):
    Generic, Create, Contain, Value, App, Page, Label = ..., ..., ..., ..., ..., ..., ...  # Wet for autocompletion

    def is_app(self):
        return self.__class__ is self.App

    def is_page(self):
        return self.__class__ is self.Page

    def __repr__(self):
        return f"<GUI {self.__class__.__name__}>"
