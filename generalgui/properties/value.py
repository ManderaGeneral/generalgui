

class PartBaseClass:
    def draw_create_hook(self, kwargs): ...

class Value(PartBaseClass):
    def __init__(self, value=None):
        """ :param generalgui.MethodGrouper self:
            :param value: """
        self._value = value

    def draw_create_hook(self, kwargs):
        kwargs["text"] = self.value
        return kwargs

    @property
    def value(self):
        """ :param generalgui.MethodGrouper self: """
        return self._value

    @value.setter
    def value(self, value):
        """ :param generalgui.MethodGrouper self: """
        self._value = "" if value is None else value
        self.draw_value()



