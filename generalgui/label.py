
from generallibrary import initBases

from generalgui import Value

@initBases
class Label(Value):
    def __init__(self, value=None, parent=None):
        pass

    generic = Value.generic
Value.generic.label = Label


