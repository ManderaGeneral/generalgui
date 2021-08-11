
from generallibrary import initBases
from generalgui import _Contain


class App(_Contain):
    """ Blank App. """
    apps = []
    def __init__(self):
        self.apps.append(self)
        self._atexit_funcs.insert(0, self.draw)



