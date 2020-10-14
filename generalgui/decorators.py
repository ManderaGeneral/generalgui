
from generallibrary import SigInfo



def _group_helper():
    def _decorator(func):
        """ Changes `self` to outer Container in possible group. """
        def _wrapper(*args, **kwargs):
            sigInfo = SigInfo(func, *args, **kwargs)

            part = sigInfo["self"]  # type: MethodGrouper
            if part.grouped_containers:
                if part != part.grouped_containers[0]:
                    sigInfo["self"] = part.grouped_containers[0]
            return sigInfo()
        return _wrapper
    return _decorator

def group_top():
    return _group_helper("top")

from generalgui import MethodGrouper








































































