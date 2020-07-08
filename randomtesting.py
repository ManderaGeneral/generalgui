"""Random testing"""

from generallibrary.time import sleep

from generalgui import App, Grid, Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet
from generalvector import Vec2

import tkinter as tk
import inspect

import pandas as pd

# grid = Grid(App())
# Label(grid, column=1, row=1)

# print(grid.getFirstEmptyPos(Vec2(1, -1), Vec2(0, -1)))


app = App()

def f():
    app.hide()
    app.widget.after(1000, app.show)

Button(Page(app), "test", f).show()





# page = Page(app)
# Button(page, value="testing")
# print(page.getElementByValue("testing"))
