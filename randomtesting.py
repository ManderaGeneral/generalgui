"""Random testing"""

from generalgui.app import App
from generalgui.page import Page
from generalgui.element import Text, Button
from generallibrary.time import sleep
import tkinter as tk

app = App()
col1 = Page(app, side="left", fill="y")
col2 = Page(app, side="left")

for page in (main := Page(col1, height=200, width=80, hsb=False)), Page(col2):
    btn = Button(page, text="hello", func=lambda: print(5))

    for i in range(30):
        Text(page, "there")
    page.showChildren(mainloop=False)


page.app.mainloop()
