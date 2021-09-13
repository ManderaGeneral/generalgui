

class Value:
    def __init__(self, value=None):
        """ :param generalgui.MethodGrouper self:
            :param value: """
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


