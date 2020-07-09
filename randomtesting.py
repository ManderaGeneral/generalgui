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
import pandas as pd
import random

df = pd.DataFrame([[random.randint(-100, 100) for _ in range(20)] for _ in range(20)])
page = Page(App())
Spreadsheet(page, cellVSB=True).loadDataFrame(df)
page.show()



# page = Page(app)
# Button(page, value="testing")
# print(page.getElementByValue("testing"))
