import tkinter as tk

from generalgui.properties.generic import Generic
from generalgui.properties.value import Value



class Button(Generic, Value):
    widget_cls = tk.Button

    def __init__(self, parent=None, value=None, bind=None):
        if bind:
            self.bind(bind)



