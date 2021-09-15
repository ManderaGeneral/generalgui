
from generallibrary import sleep, Timer

import tkinter as tk


class Draw:
    """ Idea is that Draw visualizes a TreeDiagram decoupled.
        Try to keep tkinter stuff here. """
    def __init__(self, top_part):
        """ :param any or generallibrary.TreeDiagram top_part: """
        self.top_part = top_part
        self.tk = tk.Tk()
        self.previous_parts = set()
        self.draw_all()

        self.draw_timer = Timer()
        while True:
            try:
                self.tk.update_idletasks()
                self.tk.update()
            except tk.TclError:
                exit()

            if set(self.get_parts()) != self.previous_parts:
                print("changed")
                self.draw_all()

    def get_parts(self):
        return self.top_part.get_children(depth=-1, include_self=True, gen=True)

    def draw_all(self):
        parts = set()
        for part in self.get_parts():
            self.create(part=part)
            parts.add(part)

        dead_parts = self.previous_parts - parts
        for dead_part in dead_parts:
            dead_part.widget.destroy()
        self.previous_parts = parts

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



















