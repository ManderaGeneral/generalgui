
from generallibrary import initBases

from generalgui import Generic

@initBases
class Value(Generic.Create):
    def __init__(self, value=None):
        self._value = self.set_value(value)

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value
        return value

Generic.Create.Value = Value
