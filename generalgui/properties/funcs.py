from generallibrary import getBaseClassNames, SigInfo, dict_insert, wrapper_transfer


def set_parent_hook(self, parent, _draw=True):
    """ :param generalgui.MethodGrouper self:
        :param generalgui.MethodGrouper parent: """
    if _draw:
        for part in self.get_children(depth=-1, include_self=True, gen=True):
            part.draw_create()
    assert "Contain" in getBaseClassNames(parent) or parent is None


class PartBaseClass:
    def draw_create_hook(self, kwargs):
        """ Used to decouple properties, called by draw_create which is called by init and set_parent. """
    def draw_create_post_hook(self):
        """ Called after widget is packed. """


def _deco_draw_queue(func):
    """ Append one order to dict for this func call. 
        Creates a key with id of Part and func's name. 
        If key exists as an old order then it's removed. 
        Returns key unless draw_now is True. """
    def _wrapper(*args, **kwargs):
        sigInfo = SigInfo(func, *args, **kwargs)
        methodGrouper = sigInfo["self"]
        orders = methodGrouper.orders
        key = methodGrouper.get_order_key(func)

        if sigInfo["draw_now"]:
            orders.pop(key, None)  # This allows us to manually call draw_create(draw_now=True) after instantiating a Page instead of passing draw_now to Page.
            sigInfo.call()
        else:
            orders[key] = sigInfo
            return key

        # Could possibly do something like this to skip queue instead of drawing instantly
        # if sigInfo["draw_now"]:
        #     dict_insert(orders, **{key: sigInfo})
        # else:
        #     orders[key] = sigInfo

    return wrapper_transfer(func, _wrapper)






















