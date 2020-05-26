"""Random testing"""

from generallibrary.time import sleep

from generalgui import Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet

import tkinter as tk
import inspect

import pandas as pd


def click(x):
    print(x.styleHandler.getStyle("Click").isEnabled())
    x.click()
    print(x.styleHandler.getStyle("Click").isEnabled())


page = Page()
button = Button(page, "Test", lambda: print(5))
Button(page, "click", lambda: click(button))

# button.widget.after(1000, button.click)

page.show()

# page.show(mainloop=False)
# page.app.remove()









