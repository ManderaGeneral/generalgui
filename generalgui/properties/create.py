
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

    def __call__(self, *args, **kwargs):
        self.tk_widget = self.tk_widget_cls(**self.kwargs)

    @property
    def is_packed(self):
        try:
            return self.tk_widget.winfo_manager() != ""
        except self.part.tk.TclError:
            return False

class Create:
    def __init__(self, parent=None, destroy_when_hidden=True):
        """ :param generalgui.MethodGrouper self: """
        self.widget = None
        self.destroy_when_hidden = destroy_when_hidden
        self.is_shown = True

        self._parent = None
        self.parent = parent

    @property
    def parent(self):
        return self._parent

    @parent.setter  # HERE ** Probably dont wanna do this as we should generalize it, meaning we should do the same for is_shown, i.e. setting show=True instead of show(). And for show and all those methods we're going to want to support parameters.
    def parent(self, parent):
        self._parent = self._auto_parent(parent=parent)

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

    def remove(self):
        """ Remove this part from it's parent's children and destroys widget.

            :param generalgui.MethodGrouper self: """
        if self.parent:
            self.parent.children.remove(self)

        self.widget.destroy()

    def hide(self):
        if self.is_shown:
            if self.destroy_when_hidden:
                self.widget.destroy()
            else:
                self.widget.hide()
            self.is_shown = False

    def move_to(self, parent=None):
        """ Move this part to a `Contain` parent.
            Repacks if it was packed.

            :param generalgui.MethodGrouper self:
            :param None or generalgui.MethodGrouper parent: """
        is_shown = self.is_shown
        self.remove()
        self.parent = self._auto_parent(parent=parent)
        self.parent.children.append(self)






    def widget_prepare(self, tk_widget, **kwargs):
        """ Prepare a tk widget for this Part.

            :param generalgui.MethodGrouper self:
            :param tk_widget: """
        self.widget = Widget(part=self, tk_widget=tk_widget, **kwargs)

    def show(self):
        """ :param generalgui.MethodGrouper self: """
        assert self.widget
        self.widget["master"] = self.parent
        self.widget()



    @property
    def app(self):
        """ :param generalgui.MethodGrouper self: """
        while True:
            return self if self.__class__ == self.App else self.parent.app












































