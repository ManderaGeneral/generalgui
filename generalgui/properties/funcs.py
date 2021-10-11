from generallibrary import getBaseClassNames


def set_parent_hook(self, parent):
    """ Not called from init.

        :param generalgui.MethodGrouper self:
        :param generalgui.MethodGrouper parent: """
    self.draw_create()
    assert "Contain" in getBaseClassNames(parent) or parent is None
