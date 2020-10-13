
from generallibrary import getBaseClassNames, initBases



# destroy, pack, hide, create, is_existing, is_packed, is_shown, master
class Widget:
    """ Handles one created tk widget for a Part. """
    def __init__(self, part):
        """ :param generalgui.MethodGrouper part: """
        self.part = part
        self.tk_widget = self.create()

    def create(self):
        return self.tk_widget_cls(**self.part.)

    def destroy(self):
        pass

    def pack(self):
        pass

    def hide(self):
        pass

    def is_existing(self):
        pass

    def is_packed(self):
        pass

    def is_shown(self):
        pass

    def master(self):
        pass


class Config:
    def init_config(self):
        return

    def post_config(self):
        return

    def init_config(self):
        return


class Construct:
    """ Should contain all data necessary to encode. """
    def __init__(self, parent=None):
        """ :param generalgui.MethodGrouper self: """
        self._hidden = False
        self._parent = None

        self._tk_widget_cls = None
        self._kwargs = None

        self.widget = None

        self.move_to(parent=parent)

    def widget_prepare(self, tk_widget_cls, **kwargs):
        """ Prepare a tk widget for this Part.

            :param generalgui.MethodGrouper self:
            :param tk_widget_cls: """
        self._tk_widget_cls = tk_widget_cls
        self._kwargs = kwargs

    @property
    def hidden(self):
        """ Get whether this part is hidden, ignoring if parents are hidden.

            :param generalgui.MethodGrouper self: """
        return self._hidden

    @property
    def parent(self):
        """ Get this part's parent.

            :param generalgui.MethodGrouper self: """
        return self._parent

    @property
    def is_shown(self):
        """ Get whether this part and all its parents aren't hidden.

            :param generalgui.MethodGrouper self: """
        for part in self.parents(include_self=True):
            if part.hidden:
                return False
        return True

    def remove(self):
        """ Remove this part from it's parent's children and destroys widget.

            :param generalgui.MethodGrouper self: """
        if self.parent:
            self.parent.children.remove(self)

        self._parent = None
        self.widget.destroy()

    def hide(self):
        """ :param generalgui.MethodGrouper self: """
        self._hidden = True
        if self.destroy_when_hidden:
            return self.remove()
        else:
            self.widget.hide()

    def move_to(self, parent=None):
        """ Move this part to a `Contain` parent.
            Repacks if it was packed.

            :param generalgui.MethodGrouper self:
            :param None or generalgui.MethodGrouper parent: """
        self.remove()
        self._parent = self._auto_parent(parent=parent)
        self.parent.children.append(self)
        self.show()

    def _auto_parent(self, parent=None):
        """ :param generalgui.MethodGrouper self: """
        if parent is None:
            if self.is_app:
                parent = self
            elif self.is_page:
                parent = self.App()
            else:
                parent = self.Page()
        assert "contain" in getBaseClassNames(parent)
        return parent

    def show(self):
        """ Show this part.
            If this part is

            :param generalgui.MethodGrouper self: """
        if self.widget is None:
            self.widget = Widget(part=self)

@initBases
class Create(Construct, Config):
    def __init__(self, parent=None, destroy_when_hidden=True):
        """ :param generalgui.MethodGrouper self: """
        self.widget = None
        self.destroy_when_hidden = destroy_when_hidden  # Doesn't activate if parent is hidden

    @property
    def app(self):
        """ :param generalgui.MethodGrouper self: """
        while True:
            return self if self.__class__ == self.App else self.parent.app












































