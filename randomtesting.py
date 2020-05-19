"""Random testing"""

from generalgui import Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet

import tkinter as tk
import inspect

page = Page()
# page = Page(height=400, width=400)




Label(page, "hello")
OptionMenu(page, ["red", "green", "blue"], "hello")
LabelCheckbutton(page, "yes")
LabelEntry(page, "yes", "write")
Button(page, "Click me")



spreadsheet = Spreadsheet(page)
rows = []
for _ in range(50):
    rows.append([1, 2])
spreadsheet.headerRows(["this", "is", "test"])
spreadsheet.addRows(rows)

page.show()



