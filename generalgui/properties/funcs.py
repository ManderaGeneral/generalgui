from generallibrary import getBaseClassNames, SigInfo


def set_parent_hook(self, parent):
    """ Not called from init.

        :param generalgui.MethodGrouper self:
        :param generalgui.MethodGrouper parent: """
    self.draw_create()
    assert "Contain" in getBaseClassNames(parent) or parent is None


class PartBaseClass:
    def draw_create_hook(self, kwargs):
        """ Used to decouple properties, called by draw_create which is called by init and set_parent. """


def _deco_draw_queue(func):
    def _wrapper(*args, **kwargs):
        sigInfo = SigInfo(func, *args, **kwargs)

        if sigInfo["draw_now"]:
            sigInfo.call()
        else:
            # key = getattr(sigInfo["self"], func.__name__)
            key = f"{sigInfo['self'].id}-{func.__name__}"

            orders = sigInfo["self"].orders
            if key in orders:  # Prevent duplicate orders
                del orders[key]
            orders[key] = sigInfo
    return _wrapper

