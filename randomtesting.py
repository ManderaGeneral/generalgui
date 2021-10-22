"""Random testing"""


from generalgui import Page, Label, Button, Plot
from generallibrary import getBaseClassNames, TreeDiagram

import random


def test(part):
    part.get_parent().copy_part()

def test2(part):
    # part.get_parent().copy_part()
    # part.copy_part()
    part.copy_part(part.get_parent())
    # part.draw_destroy()

    # part.set_parent(None)
    # part.shown = False
    # part.value = "hello"



plot = Plot()

# page = Page()
#
# label = Label(parent=page, value="hi")
#
# for i in range(5):
#     btn = Button(page, str(random.randint(1, 1000)))
#     btn.bind(lambda x=btn: test2(x))


"""

MVP plan for first product release
Decide on simple useful program
    Simple stock tracker to begin with
Decide on where to store it and how to distribute it
    Private GitHub for the repo
    Public mainframe that downloads exe privately?
    Simple server to handle and track users freemium?

How should package-specific gui pages be defined? I want them decoupled
    So import gui to any package that we wanna do a page for and always include it with install? Even for non-gui apps?
    Or create an additional package for any package that wants a specific page?
        This additional one would import base API package and add gui functionality on top
        Then you can chose whether to install generalstock or generalstock_gui
        File would want a GUI page though, worried about circular dependencies, should be fine, would make file a lvl 2 instead

"""


# from pprint import pprint
# pprint(Page.orders)





