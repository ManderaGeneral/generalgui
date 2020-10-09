"""Random testing"""

import tkinter as tk
from generallibrary import initBases, getBaseClasses
import pickle
import atexit


# Automatically create Page and App
# Moveable Elements and Pages, moving top page to another app's page should automatically close the first app
# Save and loadable parts. Allowing us to dynamically delete and create instead of hiding and showing
#   Three-way sync: Tkinter, GUI objects, JSON files
# Automatic packing, but not instant. Meaning creating two pages and then hiding the first one should only ever render the second one


class Generic:
    def __init__(self):
        pass

class Create:
    def __init__(self, parent=None):
        if parent is None:
            if self.__class__ == App:
                parent = self
            elif self.__class__ == Page:
                parent = App()
            else:
                parent = Page()
        assert Contain in getBaseClasses(parent)

        self.parent = parent

    @property
    def app(self):
        while True:
            return self if self.__class__ == App else self.parent.app

class Contain:
    def show(self):
        pass


@initBases
class App(Generic, Contain):
    apps = []
    def __init__(self):
        self.apps.append(self)

    @classmethod
    def mainloop(cls):
        for app in cls.apps:
            app.show()

        tk.mainloop()




@initBases
class Page(Generic, Create, Contain):
    def __init__(self, parent=None):
        pass

@initBases
class Label(Generic, Create):
    def __init__(self, parent=None, value=None):
        self.value = value



atexit.register(App.mainloop)



Label(value="hello")



# x = pickle.dumps(Label("hello"))
# y = pickle.loads(x)
# print(y.value)


# root = Tk()
# label = Label(root)
# label.pack()
# root.bind("<Motion>", lambda event: label.configure(text=f"{event.x}, {event.y}"))
# root.mainloop()


# root2.mainloop()













