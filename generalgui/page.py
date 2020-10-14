
from generallibrary import initBases, SigInfo

from generalgui.properties import Generic, Create, Contain

@initBases
class Page(Generic, Create, Contain):  # Change Page to Frame possibly, more intuitive
    def __init__(self, parent=None):
        self.widget_sig_info = SigInfo(self.tk.Frame)

Generic.Page = Page
