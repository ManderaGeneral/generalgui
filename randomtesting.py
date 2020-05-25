"""Random testing"""

from generalgui import Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet

import tkinter as tk
import inspect

import pandas as pd


page = Page(width=200, height=100)

label1 = Label(page, "hi")
label2 = Label(page, "hi")

# label1.showSiblings(mainloop=False)
page.show(mainloop=False)


page.show()
