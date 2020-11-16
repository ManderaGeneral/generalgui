
import atexit
import tkinter as tk

from generallibrary import attributes

# Type self.hook to see all available hooks with their signatures (Requires MethodGrouper definition)

class Create:
    """ Incomplete inheritence like this is possible. """
    widget = None

    def hook_create_post_create(self):
        """ Default creation behaviour.
            :param generalgui.MethodGrouper self: """
        class_map = {"Label": "Label", "Button": "Button"}
        self.widget = getattr(tk, class_map[self.__class__.__name__])(master=self.get_parent().widget)
        self.widget.pack()

class Value(Create):
    def hook_set_attribute(self, key, value, old_value):
        """ :param generalgui.MethodGrouper self:
            :param key:
            :param value:
            :param old_value: """
        # print(self.widget, key, value, old_value)
        attr_map = {"value": "text"}
        if key in attr_map:
            self.widget.config(**{attr_map[key]: value})

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



def load_cartridge(generic):
    """ Load tkinter hooks into parts and Tree diagram.
        Todo: Keep track of overriden hooks to be able to withdraw cartridge.
        Todo: Possibly wrap methods for stacking. Thinking about __init__ for example. """
    globs = globals()
    for part_cls in generic._inheriters:
        if part_cls.__name__ in globs:
            hook_cls = globs[part_cls.__name__]
            for hook_name in attributes(hook_cls):
                setattr(part_cls, hook_name, getattr(hook_cls, hook_name))

