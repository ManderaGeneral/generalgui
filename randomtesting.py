"""Random testing"""

from generalgui import Page, Button, Label, Checkbutton, Entry, LabelCheckbutton

import tkinter as tk




page = Page()
button = Button(page, "button")
label = Label(page, "label")
checkbutton = Checkbutton(page)



print(button.getSiblings())

print(page.getChildren())
