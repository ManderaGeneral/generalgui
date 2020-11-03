
from generallibrary import initBases

from generalgui import Generic

@initBases
class Label(Generic.Create.Value):
    def __init__(self, value=None, parent=None):
        pass

Generic.Label = Label


