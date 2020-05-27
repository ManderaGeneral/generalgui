"""Random testing"""

from generalgui import Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet

from generalvector import Vec2

import tkinter as tk
import inspect

import pandas as pd


def debug():
    for spreadsheet in spreadsheets:
        frame = spreadsheet.mainGrid.getBaseElement()
        # frame.parentPage.hideChildren()
        frame.gridLabels(Vec2(0, 1), frame.getGridSize() - Vec2(1), [])


def ss(func):
    for spreadsheet in spreadsheets:
        func(spreadsheet)

page = Page()

Button(page, "Rainbow", func=page.rainbow)
reset = Button(page, "Reset", func=lambda: page.rainbow(reset=True))

columnKeys = ("color", "number", "name")
Button(page, "Add row", func=lambda: ss(lambda x: x.loadDataFrame(pd.DataFrame([["red", 5, "mandera"]], columns=columnKeys))))
Button(page, "Add indexed row", func=lambda: ss(lambda x: x.loadDataFrame(pd.DataFrame([["yellow", 2, "buck"]], columns=columnKeys, index=["hello"]))))
Button(page, "Add big", func=lambda: ss(lambda x: x.loadDataFrame(pd.DataFrame(columns=[x for x in range(20)], index=[x for x in range(20)]))))
Button(page, "Small", func=lambda: ss(lambda x: x.getTopElement().widgetConfig(height=200, width=200)))
Button(page, "Big", func=lambda: ss(lambda x: x.getTopElement().widgetConfig(height=2000, width=2000)))
Button(page, "Debug", func=debug)


spreadsheets = []
spreadsheetPage = Page(page, pack=True)

for one in range(2):
    for two in range(2):
        rowPage = Page(spreadsheetPage, pack=True)
        for three in range(2):
            for four in range(2):
                if not spreadsheets:
                    spreadsheets.append(Spreadsheet(rowPage, cellVSB=one, cellHSB=two, columnKeys=three, rowKeys=four, side="left", pack=True))




# rows = []
# for i in range(20):
#     rows.append(["red", "mandera", 9, "red", "mandera", 9, "red", "manderamanderamandera", 9])
#     rows.append(["yellow", "nick", 1337, "yellow", "nick", 1337, "yellow", "nick", 1337])
# spreadsheet.loadDataFrame(pd.DataFrame(rows))

# Label(page, "Menu").widget.place(x=100, y=250)

page.show()



