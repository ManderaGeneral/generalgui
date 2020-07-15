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

from generalgui import App, Page, Spreadsheet
import random


def test():
    print(app.widget.winfo_screenwidth(), app.widget.winfo_screenheight())
    spreadsheet.setSize(app.getSize())


df = pd.DataFrame([[random.randint(-100, 100) for _ in range(20)] for _ in range(20)])
df = df.append(["hello\nthere"], ignore_index=True)

app = App()
page = Page(app)
spreadsheet = Spreadsheet(page, cellVSB=True, hideMultiline=False)
spreadsheet.loadDataFrame(df)

# spreadsheet.maximize()
spreadsheet.setSize(1000)


# spreadsheet.menu("TESTING", Maximize=test)

page.show()



# page = Page(app)
# Button(page, value="testing")
# print(page.getElementByValue("testing"))
