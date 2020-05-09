
from generallibrary.types import typeChecker
import tkinter as tk
from generalgui.shared_methods import Element_Page, Element_Page_App, Page_App

class Page(Element_Page, Element_Page_App, Page_App):
    def __init__(self, parentPage=None, name=None, side="top", removeSiblings=False):
        typeChecker(parentPage, (None, Page, App))

        if parentPage is None:
            parentPage = App()
        elif removeSiblings:
            parentPage.removeChildren()

        self.parentPage = parentPage
        self.name = name
        self.side = side

        self.widget = tk.Frame(parentPage.widget)
        setattr(self.widget, "element", self)

        self.app = parentPage.app

from generalgui.app import App


