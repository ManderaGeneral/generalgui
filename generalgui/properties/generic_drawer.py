import atexit
import tkinter as tk

from generallibrary import getBaseClasses, ObjInfo

from generalgui.properties.funcs import _deco_draw_queue


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
        app.geometry("300x200")
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
        """ Execute some orders, limit of <= 0 is limitless. """
        if not limit:
            limit = -1
        i = 0
        while True:
            if not cls.orders or i == limit:
                break
            cls.orders.pop(next(iter(cls.orders))).call()
            i += 1
            # sleep(0.1)

    @classmethod
    def update_apps(cls):
        for app in cls.apps:
            try:
                app.update_idletasks()
                app.update()
            except tk.TclError:
                cls.apps.remove(app)
                break
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

            # Decoupling properties with these hooks
            for base in getBaseClasses(self, includeSelf=True):
                draw_create_hook = getattr(base, "draw_create_hook", None)
                if draw_create_hook:
                    objInfo = ObjInfo(draw_create_hook, parent=ObjInfo(base))
                    if objInfo.defined_by_parent():
                        hook_return = draw_create_hook(self, kwargs=kwargs)
                        if hook_return is not None:
                            kwargs = hook_return

            self.widget = self.widget_cls(**kwargs)
            self.widget.pack()

    @_deco_draw_queue
    def draw_show(self):
        """ :param generalgui.MethodGrouper self: """
        if self.shown is not self.widget.winfo_ismapped():
            if self.shown:
                self.widget.pack()
            else:
                self.widget.pack_forget()


