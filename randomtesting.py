"""Random testing"""

import tkinter as tk
from generallibrary import initBases, getBaseClasses
import pickle

from generalgui import Label


# Automatically create Page and App
# Moveable Elements and Pages, moving top page to another app's page should automatically close the first app
# Save and loadable parts. Allowing us to dynamically delete and create instead of hiding and showing
#   Three-way sync: Tkinter, GUI objects, JSON files
# Automatic packing, but not instant. Meaning creating two pages and then hiding the first one should only ever render the second one




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













