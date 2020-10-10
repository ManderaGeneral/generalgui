
from generallibrary import initBases, SigInfo

from generalgui.properties import Generic, Create, Contain

@initBases
class Page(Generic, Create, Contain):
    def __init__(self, parent=None):
        self.widget_sig_info = SigInfo(self.tk.Frame)

Generic.Page = Page
