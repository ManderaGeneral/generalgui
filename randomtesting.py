"""Random testing"""

from generallibrary.time import sleep

from generalgui import App, Grid, Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet

from generalvector import Vec2

import pandas as pd

import inspect




# page = Page(App())
# label = Label("hello")
# label.pack(page)



grid = Grid(App())

grid.fillGrid(Label, Vec2(0, 0), Vec2(2, 1))
grid.fillGrid(Label, Vec2(0, 0), Vec2(2, 1))

print([grid.getGridPos(ele) for ele in grid.getChildren()])






# Label(page, "hello\nthere", hideMultiline=True).show()




