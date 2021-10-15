from generallibrary import SigInfo


class Binder:
    def __init__(self):
        self.binds = []

    def bind(self, func):
        """ :param generalgui.MethodGrouper self: """
        sigInfo = SigInfo(func)
        self.binds.append(sigInfo)
        self.draw_bind()

    def call_binds(self):
        """ :param generalgui.MethodGrouper self: """
        return tuple(sigInfo.call() for sigInfo in self.binds)
