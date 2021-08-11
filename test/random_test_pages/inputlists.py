"""Random testing"""

from generalgui import Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet, App, ElementList, InputList

from generalvector import Vec2

import tkinter as tk
import inspect

import random

import pandas as pd


def add():
    inputList.setValues({
        "random": True,
        "hello": "yellow",
        "whatever": None,
        "a number": 5.2
    })


app = App()
page = Page(app)

buttons = ElementList(page, maxFirstSteps=1)
Button(buttons, "Add", add)
Button(buttons, "Get", lambda: print(inputList.getValues()))
Button(buttons, "Clear", lambda: inputList.removeChildren())
# Button(buttons, "Test", lambda: app.widget.focus_set())

inputList = InputList(page, maxFirstSteps=4)

app.showChildren()



