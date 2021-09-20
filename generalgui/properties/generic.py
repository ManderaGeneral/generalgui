
from generallibrary import TreeDiagram, hook, getBaseClassNames, SigInfo, sleep

import tkinter as tk
import atexit


class Binder:
    def __init__(self):
        self.binds = []

    def bind(self, func):
        """ :param generalgui.MethodGrouper self: """
        sigInfo = SigInfo(func)
        self.binds.append(sigInfo)
        self.draw_bind()

    def call_binds(self):
        """ :param generalgui.MethodGrouper self: """
        return tuple(sigInfo.call() for sigInfo in self.binds)


class Indexer:
    id = 0
    instance_by_id = {}

    def __init__(self):
        self.id_assign()

    def id_assign(self):
        self.id = Indexer.id
        Indexer.id += 1
        self.instance_by_id[self.id] = self

    def id_remove(self):
        del self.instance_by_id[self.id]



def _deco_draw_queue(func):
    def _wrapper(*args, **kwargs):
        Drawer.orders.append(lambda _args=args, _kwargs=kwargs: func(*_args, **_kwargs))
    return _wrapper

class Drawer:
    orders = []
    apps = []
    registered_mainloop = None

    def __init__(self, parent=None):
        """ :param generalgui.MethodGrouper self: """
        self.widget = None
        if parent is None:
            self.draw_create()

    def create_app(self):
        app = tk.Tk()
        self.apps.append(app)
        return app

    @classmethod
    def mainloop(cls):
        while True:
            cls.draw_queue_run()

            for app in cls.apps:
                try:
                    app.update_idletasks()
                    app.update()
                except tk.TclError:
                    pass

            if not cls.apps:
                exit()

    @classmethod
    def register_mainloop(cls):
        if not cls.registered_mainloop:
            cls.registered_mainloop = atexit.register(Drawer.mainloop)

    @classmethod
    def draw_queue_run(cls):
        if cls.orders:
            for i in range(1):
                cls.orders.pop(0)()
                # sleep(0.1)

    @_deco_draw_queue
    def draw_create(self):
        """ :param generalgui.MethodGrouper self: """
        widget_master = getattr(self.widget, "master", None)
        parent_widget = getattr(self.get_parent(), "widget", None)
        print(self)  # HERE ** Allow a good way to prevent duplicate create orders
        if not widget_master or widget_master is not parent_widget:
            if widget_master:
                self.widget.destroy()
            master = parent_widget or self.create_app()

            kwargs = {"master": master}
            if hasattr(self, "value"):
                kwargs["text"] = self.value  # This could be generalized for each widget option, could put this and draw_value in value.py too
            self.widget = self.widget_cls(**kwargs)
            self.widget.pack()

    @_deco_draw_queue
    def draw_value(self):
        """ :param generalgui.MethodGrouper self: """
        if hasattr(self, "value"):
            self.widget.config(text=self.value)

    @_deco_draw_queue
    def draw_show(self):
        """ :param generalgui.MethodGrouper self: """
        if self.shown is not self.widget.winfo_ismapped():
            if self.shown:
                self.widget.pack()
            else:
                self.widget.pack_forget()

    @_deco_draw_queue
    def draw_bind(self):
        """ :param generalgui.MethodGrouper self: """
        if self.binds:
            self.widget.bind("<Button-1>", lambda e, _part=self: _part.call_binds())


class Generic(TreeDiagram, Binder, Indexer, Drawer):

    widget_cls = ...

    def __init__(self, parent):
        self.binds = []
        self._shown = True

    def __getstate__(self):  # For pickle
        self.widget = None
        # self._parents = []
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__ = state
        self.id_assign()

    def __init_subclass__(cls, **kwargs):
        if cls.widget_cls is Ellipsis:
            raise AttributeError(f"widget_cls attr is not defined for {cls}")
    repr_attrs = ("id", "value", "binds", "shown")

    # def __eq__(self, other):
    #     return repr(self) == repr(other)  # might be slow
    #
    # def __hash__(self):
    #     return super().__hash__()

    def __repr__(self):
        parts = [
            self.__class__.__name__,
        ]
        attr_dict = {key: getattr(self, key) for key in self.repr_attrs if getattr(self, key, None)}
        if attr_dict:
            parts.append(str(attr_dict))

        return f"<GUI {', '.join(parts)}>"

    def copy_part(self, parent=None):
        old_parent, old_index = self.get_parent(), self.get_index()
        self.set_parent(parent=None)

        new = self.copy_node()
        new.set_parent(parent=parent)

        self.set_parent(parent=old_parent)
        self.set_index(index=old_index)

        if parent is None:
            new.draw()

    @property
    def shown(self):
        return self._shown

    @shown.setter
    def shown(self, shown):
        self._shown = shown
        self.draw_show()

    def is_hidden_by_parent(self):
        for parent in self.get_parents(depth=-1, gen=True):
            if parent and not parent.shown:
                return True
        return False

    def is_app(self):
        return self.__class__.__name__ == "App"

    def is_page(self):
        return self.__class__.__name__ == "Page"


def container_parent_check(self, parent):
    assert "Contain" in getBaseClassNames(parent) or parent is None
    self.draw_create()


Drawer.register_mainloop()
hook(Generic.set_parent, container_parent_check)

