
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
        sigInfo = SigInfo(func, *args, **kwargs)

        if sigInfo["draw_now"]:
            sigInfo.call()
        else:
            method = getattr(sigInfo["self"], func.__name__)
            if method in Drawer.orders:  # Prevent duplicate orders
                del Drawer.orders[method]
            Drawer.orders[method] = sigInfo


    return _wrapper

from collections import OrderedDict

class Drawer:
    orders = OrderedDict()
    apps = []
    registered_mainloop = None

    def __init__(self, parent=None, draw_now=None):
        """ :param generalgui.MethodGrouper self: """
        self.widget = None
        # set_parent_hook(self=self, parent=parent)
        self.draw_create(draw_now=draw_now)
        # self.create_top_page(parent=parent)

    def create_app(self):
        """ :param generalgui.MethodGrouper self: """
        app = tk.Tk()
        self.apps.append(app)
        return app

    def create_top_page(self):
        """ :param generalgui.MethodGrouper self: """
        if self.get_parent() is None and not self.is_page():
            page = self.Page(draw_now=True)
            self.set_parent(page)
            return page

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
            order_iter = iter(cls.orders)
            for i in range(1):
                cls.orders.pop(next(order_iter)).call()
                # sleep(0.1)

    def part_delete(self):
        """ Delete part directly without queue. """
        if self.widget:
            try:
                self.widget.destroy()
            except tk.TclError:
                pass

    @_deco_draw_queue
    def draw_create(self):
        """ This one should create a widget but also destroy it.
            Syncs tkinter widget to match Part and Part parent.
            Creates App tk if self is Page and widget's master is None.

            :param generalgui.MethodGrouper self: """
        self.create_top_page()

        widget_master = getattr(self.widget, "master", None)
        parent_widget = getattr(self.get_parent(), "widget", None)
        if not widget_master or widget_master is not parent_widget:  # If current widget master does not match parent part's widget
            self.part_delete()
            master = parent_widget or self.create_app()

            # HERE ** Why is Label's parent None?
            debug(locals(), "self", "self.get_parent()", "widget_master", "parent_widget", "master")

            kwargs = {"master": master}

            # This could be generalized for each widget option, could put this and draw_value in value.py too
            # value
            if hasattr(self, "value"):
                kwargs["text"] = self.value
            # binder
            self.draw_bind()

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


class App:
    @property
    def _tk(self):
        """ :param generalgui.MethodGrouper self: """
        return getattr(self.get_parent(index=-1, depth=-1, include_self=True).widget, "master", None)

    @_deco_draw_queue
    def app_close(self):
        """ :param generalgui.MethodGrouper self: """
        if self._tk:
            self._tk.destroy()


class Generic(TreeDiagram, Binder, Indexer, Drawer, App):

    widget_cls = ...

    def __init__(self, parent, draw_now):
        self._shown = True

    def __getstate__(self):  # For pickle
        # self.widget = None
        # self._parents = []
        dict_ = self.__dict__.copy()
        dict_["widget"] = None
        return dict_

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

        # if parent is None:
        #     new.draw()

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


from generallibrary import debug

def set_parent_hook(self, parent):
    """ Not called from init.

        :param generalgui.MethodGrouper self:
        :param generalgui.MethodGrouper parent: """
    # old_parent = self.get_parent()
    # self.create_top_page(parent=parent)

    # debug(locals(), "self", "old_parent", "old_parent.get_parent()", "parent", "old_parent.get_children()")
    # if old_parent and old_parent.get_parent() is None and old_parent is not parent and old_parent.get_children() == [self]:
    #     print("yes", old_parent, old_parent.widget)
    #     old_parent.app_close()
    # else:
    #     print("no")

    self.draw_create()
    assert "Contain" in getBaseClassNames(parent) or parent is None

Drawer.register_mainloop()
hook(Generic.set_parent, set_parent_hook)

