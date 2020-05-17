"""Random testing"""

from generalgui import Page, Button, Label, Dropdown, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet

import tkinter as tk


page = Page()
# page = Page(height=400, width=400)




Label(page, "hello")
Dropdown(page, ["red", "green", "blue"])
LabelCheckbutton(page, "yes")
LabelEntry(page, "yes", "write")
Button(page, "Click me")



spreadsheet = Spreadsheet(page)



# spreadsheet.getBaseWidget().rowconfigure(0, weight=1)
spreadsheet.getBaseWidget().columnconfigure(0, weight=1)

# spreadsheet.addRows([[1, 2, 3], [4, 5, 6]])

spreadsheet.addRows("hello")



# spreadsheet.widget.rowconfigure(0, weight=1)
# spreadsheet.widget.columnconfigure(0, weight=1)



page.show()



