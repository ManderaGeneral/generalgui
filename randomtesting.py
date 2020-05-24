"""Random testing"""

from generalgui import Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet

import tkinter as tk
import inspect

import pandas as pd



page = Page()


Label(page, "hello")
OptionMenu(page, ["red", "green", "blue"], "hello")
LabelCheckbutton(page, "yes")
LabelEntry(page, "yes", "write")
Button(page, "Rainbow", func=page.rainbow)
reset = Button(page, "Reset", func=lambda: page.rainbow(reset=True))
Button(page, "click reset", func=reset.click)

columnKeys = ("color", "number", "name")
Button(page, "Add row", func=lambda: spreadsheet.loadDataFrame(pd.DataFrame([["red", 5, "mandera"]], columns=columnKeys)))
Button(page, "Add indexed row", func=lambda: spreadsheet.loadDataFrame(pd.DataFrame([["red", 5, "mandera"]], columns=columnKeys, index=["hello"])))


spreadsheet = Spreadsheet(page, cellVSB=False, cellHSB=False, columnKeys=False, rowKeys=True)


# rows = []
# for i in range(20):
#     rows.append(["red", "mandera", 9, "red", "mandera", 9, "red", "manderamanderamandera", 9])
#     rows.append(["yellow", "nick", 1337, "yellow", "nick", 1337, "yellow", "nick", 1337])
# spreadsheet.loadDataFrame(pd.DataFrame(rows))


# Label(page, "Menu").widget.place(x=100, y=250)

page.show()



