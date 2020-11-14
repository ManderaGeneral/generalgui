
import atexit
import tkinter

from generallibrary import initBases
from generalgui import App


@initBases
class App(App):
    App.Generic.tk = tkinter

    def __init__(self):
        pass

    def create(self):
        self.tk.Tk()
        atexit.register(self.tk.mainloop)
    hook_create = create

# HERE ** experimenting with cartridges, would be nice to default to tkinter cartridge somehow, being able to import directly from generalgui
