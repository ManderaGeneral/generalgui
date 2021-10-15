import atexit
import tkinter as tk
from collections import OrderedDict

from generallibrary import SigInfo, get_origin


def _deco_draw_queue(func):
    def _wrapper(*args, **kwargs):
        sigInfo = SigInfo(func, *args, **kwargs)

        if sigInfo["draw_now"]:
            sigInfo.call()
        else:
            # key = getattr(sigInfo["self"], func.__name__)
            key = f"{sigInfo['self'].id}-{func.__name__}"

            if key in Drawer.orders:  # Prevent duplicate orders
                del Drawer.orders[key]
            Drawer.orders[key] = sigInfo
    return _wrapper


class Drawer:
    orders = {}
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
    def draw_queue_run(cls, limit=None):
        """ Execute some orders, 0 is limitless. """
        if limit is None:
            limit = 0

        i = 0
        while True:
            i += 1
            if not cls.orders or i == limit:
                break
            cls.orders.pop(next(iter(cls.orders))).call()
            # sleep(0.1)

    @classmethod
    def update_apps(cls):
        for app in cls.apps:
            try:
                app.update_idletasks()
                app.update()
            except tk.TclError:
                pass
        return bool(cls.apps)

    @classmethod
    def single_loop(cls, limit=None):
        cls.draw_queue_run(limit=limit)
        return cls.update_apps()

    @classmethod
    def mainloop(cls):
        while True:
            if not cls.single_loop(limit=1):
                exit()

    @classmethod
    def register_mainloop(cls):
        if not cls.registered_mainloop:
            cls.registered_mainloop = atexit.register(Drawer.mainloop)

    @classmethod
    def unreqister_mainloop(cls):
        if cls.registered_mainloop:
            atexit.unregister(cls.registered_mainloop)

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
            kwargs = {"master": master}


            # HERE ** decouple this
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


