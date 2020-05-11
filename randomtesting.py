"""Random testing"""

from generalgui.app import App
from generalgui.page import Page
from generalgui.element import Text, Button
from generallibrary.time import sleep
import tkinter as tk


page = Page()
btn = Button(page, text="hello", func=lambda: print(5))

for i in range(30):
    Text(page, "there")


page.show()
