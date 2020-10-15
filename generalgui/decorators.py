
from generallibrary import SigInfo


def deco_set_grouped_container(**arg_and_index):
    """ Changes `self` to outermost or innermost Container in possible group. """
    def _decorator(func):
        def _wrapper(*args, **kwargs):
            sigInfo = SigInfo(func, *args, **kwargs)

            for arg_name, i in arg_and_index:
                part = sigInfo[arg_name]
                if part is not None and part.grouped_containers and part != part.grouped_containers[i]:
                    sigInfo[arg_name] = part.grouped_containers[i]

            return sigInfo()
        return _wrapper
    return _decorator


deco_group_top = deco_set_grouped_container(self=0)
deco_group_bottom = deco_set_grouped_container(self=-1)










































































