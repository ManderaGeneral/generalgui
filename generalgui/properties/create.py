
from generallibrary import getBaseClassNames, initBases

from generalgui.decorators import deco_set_grouped_container, deco_group_top


class Create_Widget:
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


class Create_Config:
    _init_args = ["cls", "master"]
    _pack_args = ["side", "grid"]
    _post_args = ["is_hidden", "cursor", "border"]
    def __init__(self):  # HERE ** Plan was to store all args as attributes. BUT: they should be protected. I dont want to make a property for each attribute.
        # WANT: Easy autocompletion for each arg
        # WANT: Ability to configure multiple
        # WANT: Automatic updating when changing a value
        # WANT: Allowing adding to args lower in hierarchy (i.e. value for Label)

        # DONT: Update after changing one of multiple values, only once
        # DONT: Rely on manual updating as it's prone for de-sync issues

        # IDEA: Remove config method, make them all attributes,
        # IDEA: Convert old Styler to a config class for generallibrary, use that here
        # Give combined lists to Config class, then add code for our purpose
        """ :param generalgui.MethodGrouper self: """
        self.tk_cls = None

    def config(self, tk_cls=None):  # Maybe we can include `is_hidden` here so that everything for encoding is stored together?
        """ Handles all widget configuration such as cls, master, side etc.
            Has to be called in each Part's dunder init.
            If an init config is changed then widget will automatically be re-created if needed.
            That allows us to change master or even cls. """
        if tk_cls is not None:  # Iterate locals instead
            self.tk_cls = tk_cls

    def get_init_config(self):
        """ Are all init configs required?

            :param generalgui.MethodGrouper self: """
        return {}

    def get_pack_config(self):
        """ :param generalgui.MethodGrouper self: """
        return {}

    def get_post_config(self):
        """ :param generalgui.MethodGrouper self: """
        return {}


class Create_Construct:
    """ Should contain all data necessary to encode. """
    def __init__(self, parent=None):
        """ :param generalgui.MethodGrouper self: """
        self._hidden = False
        self._parent = None

        self._tk_widget_cls = None

        self.move_to(parent=parent)

    @deco_group_top
    def is_hidden(self):
        """ Get whether this part is is_hidden, ignoring if parents are is_hidden.

            :param generalgui.MethodGrouper self: """
        return self._hidden

    @deco_group_top
    def parent(self):
        """ Get this part's parent.

            :param generalgui.MethodGrouper self: """
        return self._parent

    @deco_group_top
    def is_shown(self):
        """ Get whether this part and all its parents aren't is_hidden.

            :param generalgui.MethodGrouper self: """
        for part in self.parents(include_self=True):
            if part.is_hidden():
                return False
        return True

    @deco_group_top
    def remove(self):
        """ Remove this part from it's parent's children and destroys widget.

            :param generalgui.MethodGrouper self: """
        if self.parent():
            self.parent().children.remove(self)

        self._parent = None
        self.widget.destroy()

    @deco_group_top
    def hide(self):
        """ :param generalgui.MethodGrouper self: """
        self._hidden = True
        if self.destroy_when_hidden:
            return self.remove()
        else:
            self.widget.hide()

    @deco_group_top
    def move_to(self, parent=None):
        """ Move this part to a `Contain` parent.
            Repacks if it was packed.

            :param generalgui.MethodGrouper self:
            :param None or generalgui.MethodGrouper parent: """
        self.remove()
        self._auto_create_parent(parent=parent)

    @deco_set_grouped_container(self=0, parent=-1)
    def _auto_create_parent(self, parent=None):
        """ :param generalgui.MethodGrouper self: """
        if parent is None:
            if self.is_app:
                parent = self
            elif self.is_page:
                parent = self.App()
            else:
                parent = self.Page()
        assert "contain" in getBaseClassNames(parent)

        self._parent = parent
        parent.add_child(part=self)

        if not self.is_hidden():
            self.show()


    @deco_group_top
    def show(self):
        """ Show this part.
            If this part doesn't have a widget then it's created.
            If widget is hidden then it's re-packed.


            :param generalgui.MethodGrouper self: """
        if self.widget is None:
            self.widget = Widget(part=self)

        elif not self.widget.is_packed():
            self.widget.pack()

        if not self.is_shown():
            for parent in self.get_parents():
                pass
                # if parent


@initBases
class Create(Create_Construct, Create_Config, Create_Widget):
    def __init__(self, parent=None, destroy_when_hidden=True):
        """ :param generalgui.MethodGrouper self: """
        self.destroy_when_hidden = destroy_when_hidden  # Doesn't activate if parent is is_hidden

    @property
    def app(self):
        """ :param generalgui.MethodGrouper self: """
        while True:
            return self if self.__class__ == self.App else self.parent().app












































