
from generallibrary import initBases, deco_default_self_args


class Config:
    """ Generate this class? """
    _init_args = ["_cls", "_master"]
    _pack_args = ["_side", "_grid"]
    _config_args = ["_shown", "_cursor", "_border"]
    _all_args = _init_args + _pack_args + _config_args
    def __init__(self):
        for arg_name in self._all_args:
            setattr(self, arg_name, None)

        self._store_config()

    @property
    def _cls(self): return self._cls
    @property
    def _master(self): return self._master
    @property
    def _side(self): return self._side
    @property
    def _grid(self): return self._grid
    @property
    def _border(self): return self._border
    @property
    def _cursor(self): return self._cursor
    @property
    def _shown(self): return self._shown

    def _store_config(self):
        self._current_config = {arg: getattr(self, f"_{arg}") for arg in self._all_args}

    @deco_default_self_args
    def _change_args(self, _master, _foobar):
        """
        :param _master: Foo
        :param _foobar: Bar
        """
        changed_values = {key: value for key, value in locals().items() if value != getattr(self, key)}

        for key, value in changed_values.items():
            setattr(self, key, value)

        # See if we need to re-init, re-pack or re-config
        weights = {1: self._config_args, 2: self._pack_args, 3: self._init_args}
        highest_weight = 0
        for key in changed_values.values():
            for weight, l in weights.items():
                if key in l:
                    if weight > highest_weight:
                        highest_weight = weight
                    break

        [self._config, self._pack, self._create][highest_weight - 1]()
        self._store_config()

    def _create(self):
        pass

    def _pack(self):
        pass

    def _config(self):
        pass


class Widget:
    """ Contains hidden tkinter specific methods. """
    def __init__(self):
        """ :param generalgui.MethodGrouper self: """
        self._widget = None

    def _create(self):
        """ :param generalgui.MethodGrouper self: """
        pass

    def _destroy(self):
        """ :param generalgui.MethodGrouper self: """
        pass

    def _pack(self):
        """ :param generalgui.MethodGrouper self: """
        pass

    def _hide(self):
        """ :param generalgui.MethodGrouper self: """
        pass

    def _is_existing(self):
        """ :param generalgui.MethodGrouper self: """
        pass

    def _is_packed(self):
        """ :param generalgui.MethodGrouper self: """
        pass

    def _is_shown(self):
        """ :param generalgui.MethodGrouper self: """
        pass

    def _master(self):
        """ :param generalgui.MethodGrouper self: """
        pass



@initBases
class Create_Tkinter(Config, Widget):
    """ Private tkinter methods. """
    pass


























































