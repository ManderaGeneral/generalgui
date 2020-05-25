
from generalgui import Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet

import tkinter as tk
import inspect

import pandas as pd


def debug():
    pass

def ss(func):
    for spreadsheet in spreadsheets:
        func(spreadsheet)

page = Page()

Label(page, "hello")
OptionMenu(page, ["red", "green", "blue"], "hello")
LabelCheckbutton(page, "yes")
LabelEntry(page, "yes", "write")
Button(page, "Rainbow", func=page.rainbow)
reset = Button(page, "Reset", func=lambda: page.rainbow(reset=True))
Button(page, "click reset", func=reset.click)

columnKeys = ("color", "number", "name")
Button(page, "Add row", func=lambda: ss(lambda x: x.loadDataFrame(pd.DataFrame([["red", 5, "mandera"]], columns=columnKeys))))
Button(page, "Add indexed row", func=lambda: ss(lambda x: x.loadDataFrame(pd.DataFrame([["yellow", 2, "buck"]], columns=columnKeys, index=["hello"]))))
Button(page, "Small", func=lambda: ss(lambda x: x.getTopElement().widgetConfig(height=200, width=200)))
Button(page, "Big", func=lambda: ss(lambda x: x.getTopElement().widgetConfig(height=400, width=400)))
Button(page, "Debug", func=debug)


spreadsheets = []
spreadsheetPage = Page(page, pack=True)

for one in range(2):
    for two in range(2):
        rowPage = Page(spreadsheetPage, pack=True)
        for three in range(2):
            for four in range(2):
                spreadsheets.append(Spreadsheet(rowPage, cellVSB=one, cellHSB=two, columnKeys=three, rowKeys=four, side="left", pack=True))



# rows = []
# for i in range(20):
#     rows.append(["red", "mandera", 9, "red", "mandera", 9, "red", "manderamanderamandera", 9])
#     rows.append(["yellow", "nick", 1337, "yellow", "nick", 1337, "yellow", "nick", 1337])
# spreadsheet.loadDataFrame(pd.DataFrame(rows))


# Label(page, "Menu").widget.place(x=100, y=250)

page.show()



