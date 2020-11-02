
from generallibrary import initBases
from generalgui.decorators import deco_group_bottom

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


# class Contain(Contain_Group):
@initBases
class _Contain:
    def __init__(self):
        self.children = []

    @deco_group_bottom
    def _add_child(self, part):
        assert part.parent() == self
        self.children.append(part)

