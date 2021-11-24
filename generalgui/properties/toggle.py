
from generalgui.properties.funcs import _deco_draw_queue


class Toggle:
    """ Property to easily toggle a Part's attr with optional hooks. """

    def __init__(self, toggled=None):
        """ :param generalgui.MethodGrouper self:
            :param toggled: """
        self._toggled = bool(toggled)

    def _draw_toggle_hook(self):
        """ Hook to update tk when Part is toggled. """

    @_deco_draw_queue
    def _draw_toggle(self):
        self._draw_toggle_hook()

    def toggled(self):
        return self._toggled

    def toggle(self, bool_=None):
        if bool_ is None:
            bool_ = not self._toggled
        self._toggled = bool_
        self._draw_toggle()











