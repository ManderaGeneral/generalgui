
from tkinter import Tk, Frame

class Page:
    def __init__(self, master = None, name=None):
        if master is None:
            self.app = Tk()
            master = self.app

        else:
            self.app = None

        self.name = name

        self.master = master
        self.frame = Frame(master)

        self.elements = []

    def show(self):
        self.frame.pack()
        self.app.mainloop()

    def hide(self):
        self.frame.pack_forget()


