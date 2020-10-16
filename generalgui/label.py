
from generallibrary import initBases, SigInfo

from generalgui.properties import Create, Generic

@initBases
class Label(Generic, Create):
    def __init__(self, parent=None, value=None):
        self.widget_sig_info = SigInfo(self.tk.Label, master="")

        self.value = value

