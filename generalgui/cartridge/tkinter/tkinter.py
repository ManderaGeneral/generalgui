
import tkinter as tk


class Create:
    """ Incomplete inheritence like this is possible. """
    widget = None
    class_map = {"Label": "Label", "Button": "Button", "App": "Tk", "Page": "Frame"}

    init_map = {"bgcolor": "bg"}
    config_map = {}

    # HERE ** Make a class for config values to define whether they can be changed in init and/or config only

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


class Value(Create):
    init_map = {**Create.init_map, "value": "text"}


class App(Create):
    init_map = {**Create.init_map}
    del init_map["bgcolor"]

    config_map = {**Create.config_map, "bgcolor": "bg"}

    def hook_draw(self):
        """ :param generalgui.MethodGrouper self: """
        Create.hook_draw(self=self)

        if tk.mainloop not in self._atexit_funcs:
            self._atexit_funcs.append(tk.mainloop)




