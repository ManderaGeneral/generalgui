
from generallibrary import initBases

from generalgui.properties.generic import Generic

@initBases
class Label(Generic, Generic.Create, Generic.Create.Value):
    def __init__(self, value=None, parent=None):
        pass

Generic.Label = Label


