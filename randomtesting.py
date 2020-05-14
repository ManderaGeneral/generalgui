"""Random testing"""

from generalgui.app import App
from generalgui.page import Page
from generalgui.element import Text, Button, Entry
from generalgui.dropdown import Dropdown
from generallibrary.time import sleep
import tkinter as tk

page = Page()


entry = Entry(page, "hello")
Button(page, "Change default", lambda: entry.setDefault("testing"))

entry.show()




