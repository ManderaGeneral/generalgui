"""Random testing"""

# from generallibrary.time import sleep
#
# from generalgui import App, Grid, Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet
#
# from generalvector import Vec2
#
# import pandas as pd
#
# import inspect


# page = Page(App(), resizeable=True)
# label = Label(page, "hello")
#
# label.show(



# Label(page, "hello\nthere", hideMultiline=True).show()


from tkinter import Tk, Label

root = Tk()
label = Label(root)
label.pack()
root.bind("<Motion>", lambda event: label.configure(text=f"{event.x}, {event.y}"))
root.mainloop()
