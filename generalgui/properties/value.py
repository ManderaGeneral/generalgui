

class _Value:
    def __init__(self, value=None):
        self._value = None

        self.set_value(value)

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value


