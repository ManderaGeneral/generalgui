
from generalgui.properties.funcs import PartBaseClass, _deco_draw_queue

from generallibrary import SigInfo, extend_list_in_dict, unique_obj_in_list, typeChecker, hook


class Binder(PartBaseClass):
    def __init__(self):
        """ :param generalgui.MethodGrouper self: """
        self.events = {}  # type: dict[str, list[Bind]]
        self.disabled_propagations = []

    def draw_create_post_hook(self):
        """ :param generalgui.MethodGrouper self: """
        for key in self.events:
            self._tk_new_bind(key=key)

    @property
    def bound_keys(self):
        """ Shared list.
            
            :param generalgui.MethodGrouper self: """
        if "bound_keys" not in self.shared:
            self.shared["bound_keys"] = []
        return self.shared["bound_keys"]

    def _tk_bind(self, key):
        """ :param generalgui.MethodGrouper self: """
        self._tk.bind(key, lambda event: self.call_bind(event=event, key=key), add=False)

    @_deco_draw_queue
    def _tk_new_bind(self, key):
        """ Do a non-reversible one-time bind to app's Tk widget.
            Since all binds are stored in each part, it's nice if Tk doesn't have to keep track of them.
            Therefore all Tk has to do is bind the key, even if the part that caused the bind unbinds it.
            
            :param generalgui.MethodGrouper self: """
        if key not in self.bound_keys:
            self._tk_bind(key=key)
            self.bound_keys.append(key)

    def call_bind(self, key, event=None, part=None):
        """ This method is bound to _tk for any part key that is bound.
            It starts with event.widget.part and goes through all parents to call each method stored in self.events.
            It stops if it reaches App or a disabled propagation.
            
            :param generalgui.MethodGrouper self:
            :param generalgui.MethodGrouper part: """
        if not self.exists:
            return []

        if part is None:
            if event is None:
                part = self
            else:
                if not hasattr(event.widget, "part"):
                    return []
                part = event.widget.part

        if not part.exists:
            return []

        returns = []
        for part in part.get_parents(include_self=True, gen=True):
            for bind in part.events.get(key, []):
                if SigInfo(bind.func).leadingArgNames:
                    value = bind(event)
                else:
                    value = bind()

                # if value is not None:
                returns.append(value)

            if key in part.disabled_propagations:
                break
        return returns

    def set_bind_propagation(self, key, enable):
        """ Enabled or disable propagation for binds.
            Can be used to disable click animations on buttons for example.
            Make the last function called with this bind return "break" which tkinter listens to.
            All propagations are enabled by default.
            
            :param generalgui.MethodGrouper self:
            :param str key: Bind key, <Button-1> for example.
            :param bool enable: Whether to enable propagation or not. """
        unique_obj_in_list(self.disabled_propagations, key, not enable)

    def create_bind(self, key, func, add=True, name=None):
        """ Add a function to a list in dict that is called with _bindCaller().
            If a bind exists with same name and key then it's overwritten unless add is True.
            
            :param generalgui.MethodGrouper self:
            :param str key: A key from https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
            :param function or None func: A function to be called or None to unbind
            :param bool add: Add to existing binds instead of overwriting
            :param str name: Name of bind, if bind with that name exists then it's replaced
            :return: Bind
            :raises NameError: If bind name exists with another key """
        if not add:
            self.remove_bind(key)
        elif name:
            existing_bind = self.get_bind_by_name(name)
            if existing_bind:
                if existing_bind.key == key:
                    existing_bind.remove()
                else:
                    raise NameError(f"{existing_bind} is already using this name with another key")

        bind = Bind(part=self, key=key, func=func, name=name)
        extend_list_in_dict(self.events, key, bind)
        self._tk_new_bind(key=key)

        # Commented styling stuff for now
        # if typeChecker(self, "Generic", error=False) and key == "<Button-1>" and (not self.style_handler or "Hover" not in self.style_handler.all_styles):
        #     self.widget_config(cursor="hand2")
        #     self.create_style("Hover", "<Enter>", "<Leave>", bg="gray90")
        #     self.create_style("Click", "<Button-1>", "<ButtonRelease-1>", style="Hover", relief="sunken", fg="gray40")
        #     self.create_bind("<Return>", self.click)

        return bind

    def get_bind_by_name(self, name):
        """ Get a bind by name.
            
            :param str name: Name of bind
            :rtype: Bind """
        if name is None:
            raise NameError("Cannot get bind by name None")

        for key, binds in self.events.items():
            for bind in binds:
                if bind.name == name:
                    return bind

    def remove_bind(self, key, bind=None, name=None):
        """ Remove a bind by key or bind object or name.
            
            :param generalgui.MethodGrouper self:
            :param key: A key from https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
            :param Bind bind: Specific Bind to be removed
            :param str name: Specific Bind with this name to be removed """
        if key in self.events:
            if name is not None:
                for bind in self.events[key]:
                    if bind.name == name:
                        self.events[key].remove(bind)
                        break
            elif bind is not None:
                if bind in self.events[key]:
                    self.events[key].remove(bind)
            else:
                del self.events[key]

        if key in self.events and not self.events[key]:
            del self.events[key]

    def on_click(self, func, add=True):
        """ Call a function when this part is left clicked.
            
            :param generalgui.MethodGrouper self:
            :param function or None func: Any function or None to unbind
            :param add: Whether to add to functions list or replace all """
        self.create_bind(key="<Button-1>", func=func, add=add)

    def click(self, animate=True):
        """ Manually call the function that is called when this part is left clicked.
            
            :param generalgui.MethodGrouper self:
            :param animate: Whether to animate or not """
        value = self.call_bind("<Button-1>")

        if animate and self.widget:
            self.widget.after(250, lambda: self.call_bind("<ButtonRelease-1>"))
        else:
            self.call_bind("<ButtonRelease-1>")

        return value

    def on_right_click(self, func, add=True):
        """ Call a function when this part is right clicked.
            
            :param generalgui.MethodGrouper self:
            :param function or None func: Any function or None to unbind
            :param add: Whether to add to functions list or replace all """
        self.create_bind(key="<Button-3>", func=func, add=add)

    def right_click(self, animate=True):
        """ Manually call the function that is called when this part is right clicked.
            
            :param generalgui.MethodGrouper self:
            :param animate: Whether to animate or not """
        value = self.call_bind("<Button-3>")

        if animate and self.widget:
            self.widget.after(250, lambda: self.call_bind("<ButtonRelease-3>"))
        else:
            self.call_bind("<Button-3>")

        return value

class Bind:
    """ A specific bind that contains a func """
    def __init__(self, part, key, func, name=None):
        """ :param generalgui.MethodGrouper part: """
        self.part = part
        self.name = name
        self.key = key
        self.func = func

    def __repr__(self):
        return f"<Bind - Name: {self.name} - Key: {self.key}>"

    def __call__(self, *args, **kwargs):
        if self.part.exists:
            return self.func(*args, **kwargs)

    def remove(self):
        """ Remove this bind from it's part """
        self.part.remove_bind(key=self.key, bind=self)



    # --- Old bind code

    #     self.binds = []
    #
    # def draw_create_post_hook(self):
    #     """ :param generalgui.MethodGrouper self: """
    #     self.widget.bind("<Button-1>", lambda e, _part=self: _part.call_binds())
    #
    # def bind(self, func):
    #     """ :param generalgui.MethodGrouper self: """
    #     sig_info = SigInfo(func)
    #     self.binds.append(sig_info)
    #
    # def call_binds(self):
    #     """ :param generalgui.MethodGrouper self: """
    #     return tuple(sig_info.call() for sig_info in self.binds)

























