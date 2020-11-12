
from generallibrary import initBases

from generalgui import Create

@initBases
class Value(Create):
    def __init__(self, value=None):
        """ :param generalgui.MethodGrouper self:
            :param value: """
        self.storage["value"] = self.set_value(value)

    def get_value(self):
        """ :param generalgui.MethodGrouper self: """
        return self.storage["value"]

    def set_value(self, value):
        """ :param generalgui.MethodGrouper self:
            :param value: """
        self.storage["value"] = value
        return value

