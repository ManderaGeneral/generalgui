import atexit
import tkinter as tk

from generallibrary import call_base_hooks, sleep

from generalgui.properties.funcs import _deco_draw_queue


class Drawer:
    """ All draw_* methods just syncs tkinter widget to Part attribute. """

    orders = {}
    apps = []
    registered_mainloop = None

    def __init__(self, parent=None, **extra):
        """ :param generalgui.MethodGrouper self: """
        self.widget = None  # type: tk.Widget | None
        # set_parent_hook(self=self, parent=parent)
        self.extra = extra

        # self.create_top_page(parent=parent)
    
    def get_order_key(self, method):
        """ :param generalgui.MethodGrouper self: """
        return f"{self.id}-{method.__name__}"
    
    def create_app(self):
        """ :param generalgui.MethodGrouper self: """
        app = tk.Tk()
        # app.geometry("300x200")
        self.apps.append(app)
        return app

    def create_top_page(self):
        """ :param generalgui.MethodGrouper self: """
        if self.get_parent() is None and not self.is_page():
            page = self.Page()
            page.draw_create(draw_now=True)  # This will draw immediately and remove the order that set_parent made in Page init above.
            self.set_parent(page, _draw=False)  # Set new parent without calling new draw orders
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

            sigInfo = cls.orders.pop(next(iter(cls.orders)))

            methodGrouper = sigInfo["self"]
            # parent_exists = methodGrouper.get_parent() is None or methodGrouper.get_parent().exists
            if not methodGrouper.is_deleted_by_parent():
                sigInfo.call()

            i += 1
            # sleep(0.1)

    @classmethod
    def update_apps(cls):
        for app in cls.apps:
            try:
                app.update_idletasks()
                app.update()
            except tk.TclError:
            # except (tk.TclError, KeyboardInterrupt):
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
            if not cls.single_loop(limit=100):
                exit()

    @classmethod
    def register_mainloop(cls):
        if not cls.registered_mainloop:
            cls.registered_mainloop = atexit.register(Drawer.mainloop)

    @classmethod
    def unreqister_mainloop(cls):
        if cls.registered_mainloop:
            atexit.unregister(cls.registered_mainloop)

    def _draw_create_delete(self):
        """ :param generalgui.MethodGrouper self: """
        if self._exists_tk():
            try:
                self.widget.destroy()
            except tk.TclError:
                pass
            self.widget = None

    def _draw_create_create(self):
        """ :param generalgui.MethodGrouper self: """
        self.create_top_page()

        widget_master = getattr(self.widget, "master", None)
        parent_widget = getattr(self.get_parent(), "widget", None)
        if not widget_master or widget_master is not parent_widget:  # If current widget master does not match parent part's widget
            self._draw_create_delete()

            master = parent_widget or self.create_app()
            kwargs = {"master": master}

            kwargs = call_base_hooks(self, "draw_create_hook", kwargs)

            # HERE ** Something like this for pack kwargs?
            # Would be nice if we didn't have to add **extra to all subclasses
            # Would need to allow to change side dynamically post draw
            pack_kwargs = {key: value for key, value in self.extra.items() if key in ("side", "expand", "fill")}
            self.widget = self.widget_cls(**kwargs)
            self.widget.pack(**pack_kwargs)

            setattr(self.widget, "part", self)

            call_base_hooks(self, "draw_create_post_hook")

    @_deco_draw_queue
    def draw_create(self):
        """ Creates or deletes widget depending on self.exists.
            Syncs tkinter widget to match Part and Part parent.
            Creates App tk if self is Page and widget's master is None.

            :param generalgui.MethodGrouper self: """
        # if self.exists is not self._exists_tk():
        if self.exists:
            self._draw_create_create()
        else:
            self._draw_create_delete()

    @_deco_draw_queue
    def draw_show(self):
        """ Shows or hides widget depending on self.shown.

            :param generalgui.MethodGrouper self: """
        if self.shown is not self._shown_tk():
            if self.shown:
                self.widget.pack()
            else:
                self.widget.pack_forget()
    
    def clear(self):
        """ :param generalgui.MethodGrouper self: """
        self.exists = False
        self.set_parent(None)
    
    def clear_children(self):
        """ :param generalgui.MethodGrouper self: """
        for child in self.get_children():
            child.clear()
