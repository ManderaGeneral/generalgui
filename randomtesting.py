"""Random testing"""

import tkinter as tk
from generallibrary import initBases
import pickle
import atexit



class Generic:
    def __init__(self, parent):
        self.parent = parent

    @property
    def app(self):
        return

class Create:
    pass






@initBases
class Label(Generic, Create):
    def __init__(self, parent=None, value=None):
        self.value = value




x = atexit.register(print, 5)
atexit.unregister(x)

print(2)

Label("hello")




# x = pickle.dumps(Label("hello"))
# y = pickle.loads(x)
# print(y.value)


# root = Tk()
# label = Label(root)
# label.pack()
# root.bind("<Motion>", lambda event: label.configure(text=f"{event.x}, {event.y}"))
# root.mainloop()
