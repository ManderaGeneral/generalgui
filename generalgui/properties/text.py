
from generalgui.properties.funcs import PartBaseClass, _deco_draw_queue


class Text(PartBaseClass):
    def __init__(self, text=None):
        """ :param generalgui.MethodGrouper self:
            :param text: """
        self._text = text

    def draw_create_hook(self, kwargs):
        kwargs["text"] = self.text
        return kwargs

    @property
    def text(self):
        """ :param generalgui.MethodGrouper self: """
        return self._text

    @text.setter
    def text(self, text):
        """ :param generalgui.MethodGrouper self: """
        self._text = "" if text is None else text
        self.draw_text()

    @_deco_draw_queue
    def draw_text(self):
        """ :param generalgui.MethodGrouper self: """
        if hasattr(self, "_editable_tk_var_inst"):  # Coupled to Editable
            self._editable_tk_var_inst.set(self.text)
        elif hasattr(self, "text"):
            self.widget.config(text=self.text)



