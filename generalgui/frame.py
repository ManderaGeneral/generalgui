
from generallibrary import initBases, SigInfo

from generalgui.properties import Generic, Create, Contain

@initBases
class Frame(Generic, Create, Contain):  # Change Frame to Frame possibly, more intuitive
    _init_args = Create._init_args + []
    def __init__(self, parent=None):
        self.widget_sig_info = SigInfo(self.tk.Frame)

Generic.Page = Frame
