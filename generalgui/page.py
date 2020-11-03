
from generallibrary import initBases

from generalgui import Generic

@initBases
class Page(Generic.Create.Contain):
    def __init__(self, parent=None):
        pass

Generic.Page = Page
