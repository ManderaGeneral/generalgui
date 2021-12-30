"""Random testing"""


from generalgui import *
from generallibrary import getBaseClassNames, TreeDiagram, terminal, ceil, sleep, EnvVar
from generalpackager import Packager

import random

# Packager().localrepo.format_file("generalgui/properties/generic_binder.py", write=True)


PaymentPage(endpoint="http://127.0.0.1:8000/api/payment")



exit()


def test(part):
    part.get_parent().copy_part()

def test2(part):
    # part.get_parent().copy_part()
    # part.copy_part()
    part.copy_part(part.get_parent())
    # part.draw_destroy()

    # part.set_parent(None)
    # part.shown = False
    # part.text = "hello"


# I want to be able to delete a part and then create it
def create():
    x.exists = True
def delete():
    x.exists = False

def click():
    # button.rainbow()
    # new = Page()
    # Label(new, "new")
    # entry.set_parent(None)
    page.set_parent(None)

    # for part in page.get_children(include_self=True, depth=-1):
    #     print(id(part.bound_keys))


page = Page(fill="both", expand=1)  # This should happen automatically for top page (Styler?)
Button(page, "state", lambda: print(page2.exists, page2._exists_tk(), button.exists, button._exists_tk()))
Button(page, "create", create)
Button(page, "delete", delete)


page2 = Page(page)

page.on_click(lambda: print(2))

entry = Entry(page2, "hi")
entry2 = Entry(page2, "hi")
page3 = Page(page2)
button = Button(page3, "click", click)

# page2.exists = False

x = page2



# page = None
# checkbutton = Checkbutton(page, "hi")
# button = Button(parent=page, text="click me", bind=lambda: print(checkbutton.toggled()))
# button2 = Button(parent=page, text="toggle", bind=lambda: checkbutton.toggle())

# entry = Entry(page, "hi")
# button = Button(parent=page, text="click me", bind=lambda: print(entry.text))
# button2 = Button(parent=page, text="change", bind=lambda: setattr(entry, "text", "foo"))





# button = Button(text="click me")
# button = Button(text="click me", bind=lambda: checkbutton.copy_part())

# plot = Plot()


# page = Page()
#
# label = Label(parent=page, text="hi")
#
# for i in range(5):
#     btn = Button(page, str(random.randint(1, 1000)))
#     btn.bind(lambda x=btn: test2(x))


"""
Starting with platform to actually sell program (Goal is to easily be able to sell new products)
    Generate a simple gui exe
        pip install pyinstaller
        pyinstaller randomtesting.py --onefile --windowed
    [mainframe_api] Create a new private github repo
    Create a new lightsail server with django api
    Database for users to sign in and track programs
    
    Workflow uploads new exe files to lightsail
    Allow purchases when signed in
    Exe files downloadable through api when signed in
    [generalmainframe] Local mainframe gui to sign into and start up downloaded exe files (Shortcut to skip mainframe)
    [product_stock] Create actual product, analyze portfolio, stocks and whatnot
    Non-MVP: json_data in mainframe could store the whole gui as it was left when exiting, experiment with that

How are private product repos treated differently?
    Private
    Not on PiPY
    Generates exe for mainframe_api when dependency publishes
    Could be included in Mandera readme, links would only work for me though


Stock tool
    Search for a symbol
    Display stock with different periods (Smooth slider? Update dynamically so that it's intuitive when it changes)
    A graph Page could be it's own window
        Drag and drop window on another graph Page to automatically combine to see correlations etc
        

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
    Or make all pages in generalgui
        Would make gui pretty messy and not general
    Or put all specific pages in one new package
    

"""


# from pprint import pprint
# pprint(Page.orders)





