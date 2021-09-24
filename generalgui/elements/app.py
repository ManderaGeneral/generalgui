
import tkinter as tk

from generalgui.properties.generic import Generic
from generalgui.properties.contain import Contain


class App(Generic, Contain):
    widget_cls = tk.Tk

    def __init__(self):
        pass

