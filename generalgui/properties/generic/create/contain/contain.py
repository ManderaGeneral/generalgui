
from generallibrary import initBases

from generalgui import Create




@initBases
class Contain(Create):
    """ Contains all methods having to do with containing a part. """
    def __init__(self):
        self.hook_add_child = self._enable_add_child

    def _enable_add_child(self, child):
        if child.is_app():
            raise AttributeError(f"'{child}' can never be added as child.")
        elif self.is_app() and not child.is_page():
            raise AttributeError(f"'App {self} can only have Page as child, not '{child}'.")













# class Contain_Group:
#     def __init__(self):
#         self.grouped_containers = list()
#
#     def group(self, *parts):
#         """ Group this Container Part with other Container Parts.
#             Creates one list that all parts share, containing all parts starting with outer.
#
#             Grouped Containers handles methods automatically through propagation.
#
#             Examples:
#                 Creating a Part to one of the Containers will get the bottom Container as Parent.
#                 Moving a grouped Part will grab the top Container (And all its children). """
#         grouped_containers = list(parts) + [self]
#         for part in grouped_containers:
#             part.grouped_containers = grouped_containers
#         # TODO: Assert they're connected. Also want to be able to group non-containers (Imagine grabbing Label in LabelEntry to move it)
#
#     def group_dissolve(self):
#         """ Dissolves the group for all parts in it. """
#         while self.grouped_containers:
#             del self.grouped_containers[0]









