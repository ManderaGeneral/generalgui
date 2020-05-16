"""Random testing"""

from generalgui import Page, Button, Label, Dropdown, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet

import tkinter as tk


page = Page()

Label(page, "hello")
Dropdown(page, ["red", "green", "blue"])
LabelCheckbutton(page, "yes")
LabelEntry(page, "yes", "write")
Button(page, "Click me")

spreadsheet = Spreadsheet(page)

spreadsheet.addRows([1, 2, 3])

page.show()

# Spreadsheet([[1, 2, 3], [4, 5, 6]])




