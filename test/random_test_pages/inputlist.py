"""Random testing"""

from generalgui import Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet, App, ElementList, InputList

from generalvector import Vec2

import tkinter as tk
import inspect

import random

import pandas as pd

from generallibrary.functions import leadingArgsCount


def add():
    inputList.fillWithDict({
        "random": True,
        "hello": "yellow",
        "whatever": None,
        "a number": 5.2
    })


app = App()
page = Page(app)

Button(page, "Add", add)
inputList = InputList(page, maxFirstSteps=4)

app.showChildren()



