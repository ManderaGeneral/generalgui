
import atexit
import tkinter


# Type self.hook to see all available hooks with their signatures

class App:
    def hook_create(self):
        """ :param generalgui.MethodGrouper self: """
        tkinter.Tk()
        atexit.register(tkinter.mainloop)



print(locals())

classes = ("App", )  # HERE ** Get classes automatically by iterating all recursive bases of Generic and see if their cls exists in locals()

def load_cartridge(generic):
    """ Load tkinter hooks into parts and Tree diagram. """
    for hook_cls_name in classes:
        hook_cls = globals()[hook_cls_name]
        for hook_name in [x for x in dir(hook_cls) if not x.startswith("_")]:

            cls = getattr(generic, hook_cls_name)
            hook_method = getattr(hook_cls, hook_name)
            setattr(cls, hook_name, hook_method)

