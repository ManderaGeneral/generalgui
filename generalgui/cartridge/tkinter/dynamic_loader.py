
import tkinter as tk


class Draw:
    """ Idea is that Draw visualizes a TreeDiagram decoupled.
        Try to keep tkinter stuff here. """
    def __init__(self, top_part):
        """ :param any or generallibrary.TreeDiagram top_part: """
        self.top_part = top_part
        self.tk = tk.Tk()
        self.draw_all()
        self.tk.mainloop()

    def draw_all(self):
        for part in self.top_part.get_children(depth=-1, include_self=True, gen=True):
            if part.widget is None:
                self.create(part=part)

    def create(self, part):
        # tk.Label().config
        master = part.get_parent().widget if part.get_parent() else self.tk
        part.widget = part.widget_cls(master=master)


        # HERE ** These two should be defined in their respective properties somehow
        if hasattr(part, "value"):
            part.widget.config(text=part.value)

        if part.shown:
            part.widget.pack()
