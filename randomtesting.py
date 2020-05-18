"""Random testing"""

from generalgui import Page, Button, Label, Dropdown, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet

import tkinter as tk


page = Page()
# page = Page(height=400, width=400)




# Label(page, "hello")

# Dropdown(page, ["red", "green", "blue"])
# LabelCheckbutton(page, "yes")
# LabelEntry(page, "yes", "write")
# Button(page, "Click me")



spreadsheet = Spreadsheet(page)

rows = []
for _ in range(50):
    rows.append([1, 2])
spreadsheet.addRows(rows)
spreadsheet.headerRows(["this", "is", "test"])

page.show()



