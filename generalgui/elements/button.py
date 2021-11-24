import tkinter as tk

from generalgui.properties.generic import Generic
from generalgui.properties.text import Text



class Button(Generic, Text):
    widget = ...  # type: tk.Button
    widget_cls = tk.Button

    def __init__(self, parent=None, text=None, bind=None):
        if bind:
            self.bind(bind)



