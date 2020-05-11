"""Random testing"""

from generalgui.app import App
from generalgui.page import Page
from generalgui.element import Text, Button
from generallibrary.time import sleep
import tkinter as tk
import inspect


# btn = Button(page, text="hello", func=lambda event: event.widget.configure(bg="red"))


def func():
    return 5

page = Page()
btn = Button(page, text="hello", func=lambda: print(5))
text = Text(page, "there")

btn.onClick(lambda: print(2), add=True)
btn.onClick(lambda: print(3), add=True)
btn.onClick(None, add=True)
btn.onClick(None, add=True)

print(btn.click())

page.show()

