
from generallibrary import getBaseClassNames, initBases, Config, deco_default_self_args
from generalgui.decorators import deco_set_grouped_container, deco_group_top



from generallibrary import SigInfo


class Tkinter_Config:
    """ Generate this class? """
    _init_args = ["cls", "master"]
    _pack_args = ["side", "grid"]
    _config_args = ["is_hidden", "cursor", "border"]
    _all_args = _init_args + _pack_args + _config_args
    def __init__(self):
        self._master = None

        self.current_config = {arg: getattr(self, f"_{arg}") for arg in self._all_args}

    @deco_default_self_args
    def _change_args(self, _master, _foobar):
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

        if highest_weight == 3:
            self.init()
        elif highest_weight == 2:
            self.pack()
        elif highest_weight == 1:
            self.config()

    def _master(self):
        pass

    def _event_init(self):
        pass

    def _event_pack(self):
        pass

    def _event_config(self):
        pass

# Tkinter_Config()._change_args()

class Create_Tkinter(Tkinter_Config):
    """ Contains hidden tkinter specific methods. """
    def __init__(self):
        """ :param generalgui.MethodGrouper self: """
        self.tk_widget = None

    def _create(self):
        """ :param generalgui.MethodGrouper self: """
        self.tk_widget = self.tk_cls(**self.part.get_init_config())

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


class Create_Construct:
    """ Should contain all data necessary to encode. """
    def __init__(self, parent=None):
        """ :param generalgui.MethodGrouper self: """
        self._shown = False
        self._parent = None

        self._tk_widget_cls = None

        self.move_to(parent=parent)

    @deco_group_top
    def get_parent(self):
        """ Get this part's parent.

            :param generalgui.MethodGrouper self: """
        return self._parent

    @deco_group_top
    def set_parent(self, parent):
        """ Get this part's parent.

            :param generalgui.MethodGrouper self:
            :param parent: """
        return self._parent


class Create_Relations:
    """ . """
    pass


class Create_Store:
    """ . """
    pass


@initBases
class Create(Create_Construct, Create_Tkinter, Create_Relations, Create_Store):
    def __init__(self, parent=None, destroy_when_hidden=True):
        """ :param generalgui.MethodGrouper self: """
        self.destroy_when_hidden = destroy_when_hidden  # Doesn't activate if parent is is_hidden

    @property
    def app(self):
        """ :param generalgui.MethodGrouper self: """
        while True:
            return self if self.__class__ == self.App else self.parent().app









































