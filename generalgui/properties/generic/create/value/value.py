
from generallibrary import initBases

from generalgui import _Create


class _Value(_Create):
    def __init__(self, value=None):
        """ :param generalgui.MethodGrouper self:
            :param value: """
        self.value = self.data_keys_add("value", value)

