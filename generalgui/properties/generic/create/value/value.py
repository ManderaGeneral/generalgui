
from generallibrary import initBases

from generalgui import Create

@initBases
class Value(Create):
    def __init__(self, value=None):
        self._value = self.set_value(value)

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value
        return value

    generic = Create.generic
Create.generic.contain = Value
