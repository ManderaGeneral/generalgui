
from generallibrary import getBaseClassNames


class Widget:
    def __init__(self, part, tk_widget_cls, **kwargs):
        self.part = part
        self.tk_widget_cls = tk_widget_cls
        self.kwargs = kwargs
        self.tk_widget = None

    def __getitem__(self, item):
        return self.kwargs[item]

    def __setitem__(self, key, value):
        self.kwargs[key] = value

    def create(self, *args, **kwargs):
        self.tk_widget = self.tk_widget_cls(**self.kwargs)

    def is_packed(self):
        pass

    def destroy(self):
        pass

    def hide(self):
        pass

class Create:
    def __init__(self, parent=None, destroy_when_hidden=True):
        """ :param generalgui.MethodGrouper self: """
        self.widget = None
        self.destroy_when_hidden = destroy_when_hidden  # Doesn't activate if parent is hidden

        self._hidden = True
        self._parent = None
        self.move_to(parent=parent)

    @property
    def hidden(self):
        """ Get whether this part is hidden, ignoring if parents are hidden. """
        return self._hidden

    @property
    def parent(self):
        """ Get this part's parent. """
        return self._parent

    @property
    def is_shown(self):
        """ Get whether this part and all its parents aren't hidden. """
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






    def widget_prepare(self, tk_widget, **kwargs):
        """ Prepare a tk widget for this Part.

            :param generalgui.MethodGrouper self:
            :param tk_widget: """
        self.widget = Widget(part=self, tk_widget=tk_widget, **kwargs)

    def show(self):
        """ Show this part.
            If this part is

            :param generalgui.MethodGrouper self: """
        assert self.widget

        self.widget["master"] = self.parent

        self.widget.create()



    @property
    def app(self):
        """ :param generalgui.MethodGrouper self: """
        while True:
            return self if self.__class__ == self.App else self.parent.app












































