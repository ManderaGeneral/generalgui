"""Random testing"""

from generalgui import Page, Button, Entry, LabelCheckbutton

import tkinter as tk




page = Page()

labelEntry = LabelCheckbutton(page, "Name:")
Button(page, "Click me", lambda: labelEntry.label.setValue(labelEntry.checkbutton.getValue()))


page.show()

