
from generallibrary.types import typeChecker
import tkinter as tk

class Page:
    def __init__(self, parentPage=None, name=None, side="top"):
        typeChecker(parentPage, (None, Page, App))
        self.side = side
        if parentPage is None:
            parentPage = App()

        self.parentPage = parentPage
        self.widget = tk.Frame(parentPage.widget)
        self.name = name

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

    def getApp(self):
        parentPages = self.getParentPages()
        if parentPages:
            topPage = parentPages[-1]
        else:
            topPage = self
        return topPage.parentPage

    def show(self, mainloop=True):
        for page in self.getParentPages(includeSelf=True):
            page.widget.pack(side=page.side)

        if mainloop:
            self.getApp().widget.mainloop()

    def hide(self):
        self.widget.pack_forget()


from generalgui.app import App


