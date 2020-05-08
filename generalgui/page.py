
from generallibrary.types import typeChecker
import tkinter as tk

class Page:
    def __init__(self, parentPage=None, name=None, side="top"):
        typeChecker(parentPage, (None, Page, App))
        if parentPage is None:
            parentPage = App()

        self.parentPage = parentPage
        self.name = name
        self.side = side

        self.widget = tk.Frame(parentPage.widget)
        self.app = parentPage.app

    def getParentPages(self, includeSelf=False):
        pages = [self]
        while True:
            parentPage = pages[-1].parentPage
            if isinstance(parentPage, App):
                if includeSelf:
                    return pages
                else:
                    return pages[1:]
            else:
                pages.append(parentPage)

    def getTopPage(self):
        parentPages = self.getParentPages()
        if parentPages:
            topPage = parentPages[-1]
        else:
            topPage = self
        return topPage

    def isShown(self):
        return self.widget.winfo_ismapped()

    def show(self):
        for page in self.getParentPages(includeSelf=True):
            if page.isShown():
                return
            page.widget.pack(side=page.side)

        self.app.show()

    def hide(self):
        if self.isShown():
            self.widget.pack_forget()

    def toggle(self):
        if self.isShown():
            self.hide()
        else:
            self.show()


from generalgui.app import App


