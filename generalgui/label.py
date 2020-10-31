
from generallibrary import initBases

from generalgui.properties import Create, Generic

@initBases
class Label(Generic, Create):
    def __init__(self, parent=None, value=None):

        self.config()

        self.value = value

