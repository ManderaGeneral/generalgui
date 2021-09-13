

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

        # This isn't really how I wanna do it, this syncing is prone to failure
        # if getattr(self, "widget"):
        #     self.widget.config(text=value)


