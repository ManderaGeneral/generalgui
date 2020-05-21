"""Random testing"""

from generalgui import Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet

import tkinter as tk
import inspect


x = {"a": 5}

for key, value in x.items():
    value = 3
print(x)



page = Page()
# page = Page(height=400, width=400)


Label(page, "hello")
OptionMenu(page, ["red", "green", "blue"], "hello")
LabelCheckbutton(page, "yes")
LabelEntry(page, "yes", "write")
Button(page, "Click me", func=page.rainbow)
reset = Button(page, "Reset", func=lambda: page.rainbow(reset=True))
Button(page, "click reset", func=reset.click)


spreadsheet = Spreadsheet(page)
rows = []
# for _ in range(20):
    # rows.append([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2])
    # rows.append([1, 2, 1, "randoom", 1, 2, 1, 2, 1, 2, 1, 2])

rows.append(["red", "mandera", 9])
rows.append(["yellow", "nick", 1337])

spreadsheet.headerRows(["color", "n", "number"])
spreadsheet.addRows(rows)

# page.app.widget.update()
spreadsheet.syncWidths()
# page.app.widget.update()
# spreadsheet.syncWidths()


page.show()



