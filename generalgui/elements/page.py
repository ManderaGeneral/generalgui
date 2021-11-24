
import tkinter as tk

from generalgui.properties.generic import Generic
from generalgui.properties.contain import Contain


class Page(Generic, Contain):
    widget = ...  # type: tk.Frame
    widget_cls = tk.Frame

    def __init__(self, parent=None):
        pass

Generic.Page = Page
