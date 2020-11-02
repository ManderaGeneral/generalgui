
from generalgui.properties.generic import Generic


class App(Generic):
    apps = []
    def __init__(self):
        self.apps.append(self)

Generic.App = App


