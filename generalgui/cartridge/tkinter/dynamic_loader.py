
from generallibrary import sleep, Timer, subtract_list

import tkinter as tk


class Draw:
    """ Idea is that Draw visualizes a TreeDiagram decoupled.
        Try to keep tkinter stuff here. """
    draws = []

    def __init__(self, top_part):
        """ :param any or generallibrary.TreeDiagram top_part: """
        self.tk = tk.Tk()
        self.draws.append(self)

        self.top_part_target = top_part
        self.top_part_current = None

        self.previous_parts = []
        self.draw_all()

        self.mainloop()

    def mainloop(self):
        if len(self.draws) == 1:
            while True:  # Only the latest Draw while True loop will be active
                for draw in self.draws:
                    try:
                        draw.tk.update_idletasks()
                        draw.tk.update()
                    except tk.TclError:
                        pass

                    self.draw_all()

                if not self.draws:
                    exit()

    def get_parts_gen(self):
        return self.top_part.get_children(depth=-1, include_self=True, gen=True)

    def get_parts(self):
        return list(self.get_parts_gen())

    def draw_all(self):
        parts = [self.create(part=part) for part in self.get_parts_gen()]
        dead_parts = subtract_list(self.previous_parts, parts)
        for dead_part in dead_parts:
            if dead_part.widget:
                # print("destroyed", dead_part)
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

        return part


















