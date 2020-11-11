
from generallibrary import initBases

from generalgui import Contain

@initBases
class App(Contain):
    apps = []
    def __init__(self):
        self.apps.append(self)



