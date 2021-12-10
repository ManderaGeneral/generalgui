
from generalgui.properties.funcs import PartBaseClass, _deco_draw_queue

from generallibrary import SigInfo


class Binder(PartBaseClass):
    def __init__(self):
        self.binds = []

    def draw_create_post_hook(self):
        """ :param generalgui.MethodGrouper self: """
        self.widget.bind("<Button-1>", lambda e, _part=self: _part.call_binds())

    def bind(self, func):
        """ :param generalgui.MethodGrouper self: """
        sigInfo = SigInfo(func)
        self.binds.append(sigInfo)

    def call_binds(self):
        """ :param generalgui.MethodGrouper self: """
        return tuple(sigInfo.call() for sigInfo in self.binds)
