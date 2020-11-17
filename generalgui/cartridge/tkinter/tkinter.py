
import atexit
import tkinter as tk


class Create:
    """ Incomplete inheritence like this is possible. """
    widget = None
    class_map = {"Label": "Label", "Button": "Button"}
    attr_map = {"value": "text"}

    def hook_create_post_create(self):
        """ Default creation behaviour.

            :param generalgui.MethodGrouper self: """
        tk_cls = getattr(tk, self.class_map[self.__class__.__name__])
        self.widget = tk_cls(master=self.get_parent().widget)
        self.widget.pack()

class Value(Create):
    def hook_set_attribute(self, key, value, old_value):
        """ :param generalgui.MethodGrouper self:
            :param key:
            :param value:
            :param old_value: """
        if key in self.attr_map:
            self.widget.config(**{self.attr_map[key]: value})

class App(Create):
    def hook_create_post_create(self):
        """ :param generalgui.MethodGrouper self: """
        self.widget = tk.Tk()
        atexit._clear()
        atexit.register(tk.mainloop)

class Page(Create):
    def hook_create_post_create(self):
        """ :param generalgui.MethodGrouper self: """
        self.widget = tk.Frame(master=self.get_parent().widget)
        self.widget.pack()


