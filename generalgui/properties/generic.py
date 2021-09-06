
from generallibrary import TreeDiagram


class Generic(TreeDiagram):
    def is_app(self):
        return self.__class__.__name__ == "App"

    def is_page(self):
        return self.__class__.__name__ == "Page"

    def __repr__(self):
        return f"<GUI {self.__class__.__name__}>"
