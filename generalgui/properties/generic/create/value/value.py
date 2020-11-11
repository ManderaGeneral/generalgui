
from generallibrary import initBases

from generalgui import Create

@initBases
class Value(Create):
    def __init__(self, value=None):
        """ :param generalgui.MethodGrouper self:
            :param value: """
        self._value = self.set_value(value)
        self.store_add("value", self.get_value, self.set_value)

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value
        return value

