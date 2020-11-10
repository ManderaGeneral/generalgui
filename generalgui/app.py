
from generallibrary import initBases

from generalgui import Generic

@initBases
class App(Generic):
    apps = []
    def __init__(self):
        self.apps.append(self)

    generic = Generic
Generic.app = App


