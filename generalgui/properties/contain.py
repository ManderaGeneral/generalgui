
from generallibrary import initBases

class Contain_Group:
    def __init__(self):
        self.grouped_containers = []

    def group(self, *parts):
        """ Group this Container Part with other Container Parts.
            Creates one list that all parts share, containing all parts starting with outer.

            Grouped Containers handles methods automatically through propagation.

            Examples:
                Creating a Part to one of the Containers will get the bottom Container as Parent.
                Moving a grouped Part will grab the top Container (And all its children). """

@initBases
class Contain(Contain_Group):
    def __init__(self):
        self.children = []

