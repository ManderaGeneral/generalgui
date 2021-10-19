
from generalgui.properties.funcs import PartBaseClass, _deco_draw_queue


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

    @_deco_draw_queue
    def draw_value(self):
        """ :param generalgui.MethodGrouper self: """
        if hasattr(self, "value"):
            self.widget.config(text=self.value)



