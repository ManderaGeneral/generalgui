
from generallibrary import initBases

from generalgui import Create


@initBases
class Value(Create):
    def __init__(self, value=None):
        """ :param generalgui.MethodGrouper self:
            :param value: """
        self.data_keys.append("value")
        self.value = value

