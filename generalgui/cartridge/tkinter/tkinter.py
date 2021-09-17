
import tkinter as tk


class _DataKey:
    def __init__(self, name, tk_name, inittable, configurable):
        self.name = name
        self.tk_name = tk_name
        self.inittable = inittable
        self.configurable = configurable

class DataKeys:
    """ Connects to diagram's data_keys through hook_set_attribute().
        Easily see if a data_key can be updated to tkinter widget by config or if it has to be re-created. """
    def __init__(self):
        self.attrs = []

    def add(self, name, tk_name, inittable, configurable):
        if name not in self.names:
            self.attrs.append(_DataKey(name, tk_name, inittable, configurable))

    @property
    def names(self):
        return [attr.name for attr in self.attrs]




class _Create:
    """ Incomplete inheritence like this is possible. """
    widget = None
    class_map = {"Label": "Label", "Button": "Button", "App": "Tk", "Page": "Frame"}


    init_map = {"bgcolor": "bg"}
    config_map = {}

    attrs = DataKeys()
    attrs.add(name="bgcolor", tk_name="bg", inittable=True, configurable=True)

    def __init__(self):
        print(getattr(self, "original_methods")["_Create"]["__init__"])



    def hook_draw(self):
        """ Default draw behaviour.

            :param generalgui.MethodGrouper self: """
        tk_cls = getattr(tk, self.class_map[self.__class__.__name__])
        init_args = {self.init_map[key]: value for key, value in self.data.items() if value and key in self.init_map}

        if not self.is_app():
            init_args["master"] = self.get_parent().widget

        self.widget = tk_cls(**init_args)

        config_args = {self.config_map[key]: value for key, value in self.data.items() if value and key in self.config_map}
        self.widget.config(**config_args)

        if not self.is_app():
            self.widget.pack()


    def hook_set_attribute(self, key, value, old_value):
        """ :param generalgui.MethodGrouper self:
            :param key:
            :param value:
            :param old_value: """
        if self.widget:
            if key in self.config_map:  # Todo: Add init_map
                self.widget.config(**{self.config_map[key]: value})


class _Value(_Create):
    init_map = {**_Create.init_map, "value": "text"}

    # attrs.add(name="bgcolor", tk_name="bg", inittable=True, configurable=True)


class App(_Create):
    init_map = {**_Create.init_map}
    del init_map["bgcolor"]

    config_map = {**_Create.config_map, "bgcolor": "bg"}

    def hook_draw(self):
        """ :param generalgui.MethodGrouper self: """
        _Create.hook_draw(self=self)

        if tk.mainloop not in self._atexit_funcs:
            self._atexit_funcs.append(tk.mainloop)



