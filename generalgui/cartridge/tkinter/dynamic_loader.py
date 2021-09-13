
from generallibrary import sleep

import tkinter as tk


class Draw:
    """ Idea is that Draw visualizes a TreeDiagram decoupled.
        Try to keep tkinter stuff here. """
    def __init__(self, top_part):
        """ :param any or generallibrary.TreeDiagram top_part: """
        self.last_draw_hash = None
        self.top_part = top_part
        self.tk = tk.Tk()
        self.draw_all()
        while True:
            try:
                self.tk.update_idletasks()
                self.tk.update()
            except tk.TclError:
                exit()

            if self.get_draw_hash() != self.last_draw_hash:
                print("changed")
                self.draw_all()

    def draw_all(self):
        # HERE ** Maybe create a set of all widgets and store previous one too.
        # Easily compare to get widgets left behind
        for part in self.top_part.get_children(depth=-1, include_self=True, gen=True):
            self.create(part=part)
        self.last_draw_hash = self.get_draw_hash()

    def get_draw_hash(self):
        return self.top_part.view(print_out=False)

    def create(self, part):
        # tk.Label().config
        if part.widget is None:
            master = part.get_parent().widget if part.get_parent() else self.tk
            part.widget = part.widget_cls(master=master)

        if hasattr(part, "value"):
            part.widget.config(text=part.value)

        if part.shown is not part.widget.winfo_ismapped():
            if part.shown:
                part.widget.pack()
            else:
                part.widget.pack_forget()

        if part.binds:
            part.widget.bind("<Button-1>", lambda e, _part=part: _part.call_binds())



















