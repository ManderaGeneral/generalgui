"""Random testing"""

from generalgui import Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet, App, ElementList

from generalvector import Vec2

import tkinter as tk
import inspect




import random

import pandas as pd

from generallibrary.functions import leadingArgsCount


def debug():
    for spreadsheet in spreadsheets:
        spreadsheet._syncColumnKeysWidth(True)
        # frame = spreadsheet.mainGrid.getBaseElement()
        # frame.parentPage.hideChildren()
        # frame.gridLabels(Vec2(0, 1), frame.getGridSize() - Vec2(1), [])

def ss(func):
    for spreadsheet in spreadsheets:
        func(spreadsheet)

def addBig():
    l = []
    for x in range(10):
        l.append([])
        for y in range(10):
            l[-1].append(random.randint(-100, 100))

    df = pd.DataFrame(l)

    ss(lambda x: x.loadDataFrame(df))

app = App()
page = ElementList(app, maxFirstSteps=4)

Button(page, "Rainbow", onClick=app.rainbow)
reset = Button(page, "Reset", onClick=lambda: app.rainbow(reset=True))

columnKeys = ("color", "number", "name")
Button(page, "Add row", onClick=lambda: ss(lambda x: x.loadDataFrame(pd.DataFrame([["red", 5, "mandera"]], columns=columnKeys))))
Button(page, "Add indexed row", onClick=lambda: ss(lambda x: x.loadDataFrame(pd.DataFrame([["yellow", 2, "buck"], ["blue", 5, "zole"]], columns=columnKeys, index=["hello", "there"]))))
Button(page, "Add big", onClick=addBig)
Button(page, "Small", onClick=lambda: ss(lambda x: x.getTopElement().widgetConfig(height=200, width=200)))
Button(page, "Big", onClick=lambda: ss(lambda x: x.getTopElement().widgetConfig(height=2000, width=2000)))
Button(page, "Debug", onClick=debug)
# Page(page, height=100, pack=True)
LabelEntry(page, "testing")
LabelCheckbutton(page, "testing this one")



page = Page(app)

spreadsheets = []
spreadsheetPage = Page(page, pack=True)
# spreadsheetPage = Page(page, pack=True, width=1000, height=1000, hsb=True, vsb=True, resizeable=True)

for one in range(2):
    for two in range(2):
        rowPage = Page(spreadsheetPage, pack=True)
        for three in range(2):
            for four in range(2):
                # if not spreadsheets:
                #     spreadsheets.append(Spreadsheet(rowPage, cellVSB=True, cellHSB=True, columnKeys=True, rowKeys=False, side="left", pack=True))
                spreadsheets.append(Spreadsheet(rowPage, cellVSB=one, cellHSB=two, columnKeys=three, rowKeys=four, side="left", pack=True))




# rows = []
# for i in range(20):
#     rows.append(["red", "mandera", 9, "red", "mandera", 9, "red", "manderamanderamandera", 9])
#     rows.append(["yellow", "nick", 1337, "yellow", "nick", 1337, "yellow", "nick", 1337])
# spreadsheet.loadDataFrame(pd.DataFrame(rows))

# Label(page, "Menu").widget.place(x=100, y=250)

app.showChildren()



