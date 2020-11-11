
from generallibrary import initBases

from generalgui import Create


class _Contain_Relations:
    def __init__(self):
        """ :param generalgui.MethodGrouper self: """
        self.storage["children"] = []

    def add_child(self, part):
        """ Add a createable child to this container. Chained with Create.set_parent().

            :param generalgui.MethodGrouper self:
            :param generalgui.Create part: """
        if part.get_parent() == self:
            self.storage["children"].append(part.storage)
        else:
            part.set_parent(self)

    def all_children(self):
        """ :param generalgui.MethodGrouper self: """
        return [child_storage["_instance"] for child_storage in self.storage["children"]]


@initBases
class Contain(Create, _Contain_Relations):
    """ Contains all methods having to do with containing a part. """














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









