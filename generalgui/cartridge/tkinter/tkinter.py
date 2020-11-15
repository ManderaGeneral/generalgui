
import atexit
import tkinter


def create(self):
    """ :param generalgui.MethodGrouper self: """
    if self.is_app():
        tkinter.Tk()
        atexit.register(tkinter.mainloop)


def load_cartridge(cls):
    """ Load tkinter hooks into parts and Tree diagram. """
    cls.hook_create = create
