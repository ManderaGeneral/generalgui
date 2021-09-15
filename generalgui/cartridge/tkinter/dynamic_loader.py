
from generallibrary import sleep, Timer

import tkinter as tk


class Draw:
    """ Idea is that Draw visualizes a TreeDiagram decoupled.
        Try to keep tkinter stuff here. """

    draws = []

    def __init__(self, top_part):
        """ :param any or generallibrary.TreeDiagram top_part: """
        self.tk = tk.Tk()
        self.draws.append(self)

        self.top_part = top_part
        self.previous_parts = set()
        self.draw_all()

        self.mainloop()

    def mainloop(self):
        if len(self.draws) == 1:
            while True:
                for draw in self.draws:
                    try:
                        draw.tk.update_idletasks()
                        draw.tk.update()
                    except tk.TclError:
                        pass

                    if set(draw.get_parts()) != draw.previous_parts:
                        print("changed")
                        draw.draw_all()
                if not self.draws:
                    exit()

    def get_parts(self):
        return self.top_part.get_children(depth=-1, include_self=True, gen=True)

    def draw_all(self):
        parts = set()  # HERE ** Don't think we can use set as we need to allow duplicating nodes, maybe add something to repr? index?
        for part in self.get_parts():
            self.create(part=part)
            parts.add(part)

        dead_parts = self.previous_parts - parts
        for dead_part in dead_parts:
            if dead_part.widget:
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



















