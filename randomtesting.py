"""Random testing"""

from generalgui.app import App
from generalgui.page import Page
from generalgui.element import Text, Button, Dropdown
from generallibrary.time import sleep
import tkinter as tk



page = Page()

btn = Button(page, "Click")

print(btn.widget.keys())

dropdown = Dropdown(page, ["red", "blue", "green"], func=lambda event: print(event))

page.show()
