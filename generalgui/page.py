
from generallibrary import initBases

from generalgui.properties.generic import Generic

@initBases
class Page(Generic, Generic.Create, Generic.Create.Contain):
    def __init__(self, parent=None):
        pass

Generic.Page = Page
