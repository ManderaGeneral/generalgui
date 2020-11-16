
import atexit
import tkinter

from generallibrary import attributes

# Type self.hook to see all available hooks with their signatures

class App:
    def hook_create(self):
        """ :param generalgui.MethodGrouper self: """
        tkinter.Tk()
        atexit.register(tkinter.mainloop)


def load_cartridge(generic):
    """ Load tkinter hooks into parts and Tree diagram. """
    globs = globals()
    for part_cls in generic._inheriters:
        if part_cls.__name__ in globs:
            hook_cls = globs[part_cls.__name__]
            for hook_name in attributes(hook_cls):
                setattr(part_cls, hook_name, getattr(hook_cls, hook_name))

