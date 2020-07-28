"""Random testing"""

from generallibrary.time import sleep

from generalgui import App, Grid, Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet

from generalvector import Vec2

import pandas as pd

import inspect







page = Page(App(), resizeable=True)
label = Label(page, "hello")

label.show()







# Label(page, "hello\nthere", hideMultiline=True).show()




