
from generallibrary import initBases

from generalgui import Create


@initBases
class Value(Create):
    def __init__(self, value=None):
        """ :param generalgui.MethodGrouper self:
            :param value: """
        self.value = self.data_keys_add("value", value)

