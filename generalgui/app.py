
from generallibrary import initBases

from generalgui import Contain

@initBases
class App(Contain):
    apps = []
    def __init__(self, test=None):
        self.apps.append(self)

        self.data_keys.append("test")
        self.test = test

    def create(self):
        print(self.test)

    # hook_create = create

