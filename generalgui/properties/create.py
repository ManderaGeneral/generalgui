
from generallibrary import getBaseClassNames


class Widget:
    def __init__(self, part, tk_widget, **kwargs):
        self.part = part
        self.tk_widget = tk_widget
        self.kwargs = kwargs

    def __getitem__(self, item):
        return self.kwargs[item]

    def __setitem__(self, key, value):
        self.kwargs[key] = value

    def __call__(self, *args, **kwargs):
        return self.tk_widget(**self.kwargs)

    @property
    def is_packed(self):
        return

class Create:
    def __init__(self, parent=None):
        """ :param generalgui.MethodGrouper self: """
        self.widget = None
        self.parent = None

        self.move_to(parent=parent)

    def remove(self):
        """ Remove this part from it's parent's children and unpacks if packed.

            :param generalgui.MethodGrouper self: """
        if self.parent:
            self.parent.children.remove(self)
        if self.widget.is_packed:
            self.widget.unpack()

    def move_to(self, parent=None):
        """ Move this part to a `Contain` parent.
            Repacks if it was packed.

            :param generalgui.MethodGrouper self:
            :param None or generalgui.MethodGrouper parent: """
        self.remove()
        self.parent = self._auto_parent(parent=parent)
        self.parent.children.append(self)

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
        """ :param generalgui.MethodGrouper self: """
        assert self.widget
        self.widget["master"] = self.parent
        self.widget()



    @property
    def app(self):
        """ :param generalgui.MethodGrouper self: """
        while True:
            return self if self.__class__ == self.App else self.parent.app












































