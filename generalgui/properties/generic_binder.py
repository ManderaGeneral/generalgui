
from generalgui.properties.funcs import PartBaseClass, _deco_draw_queue

from generallibrary import SigInfo


class Binder(PartBaseClass):
    def __init__(self):
        self.binds = []

    def draw_create_hook(self, kwargs):
        """ :param generalgui.MethodGrouper self: """
        self.draw_bind()

    def bind(self, func):
        """ :param generalgui.MethodGrouper self: """
        sigInfo = SigInfo(func)
        self.binds.append(sigInfo)
        self.draw_bind()

    def call_binds(self):
        """ :param generalgui.MethodGrouper self: """
        return tuple(sigInfo.call() for sigInfo in self.binds)

    @_deco_draw_queue
    def draw_bind(self):
        """ :param generalgui.MethodGrouper self: """
        if self.binds:
            self.widget.bind("<Button-1>", lambda e, _part=self: _part.call_binds())
