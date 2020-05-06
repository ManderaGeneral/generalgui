
from generallibrary.types import typeChecker
import tkinter as tk

class Page:
    def __init__(self, parentPage=None, name=None):
        typeChecker(parentPage, (None, Page))

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
        return self.getParentPages()[-1].parentPage.widget

    def show(self):
        for page in (pages := self.getParentPages(includeSelf=True)):
            page.widget.pack()

        pages[-1].parentPage.widget.mainloop()

    def hide(self):
        self.widget.pack_forget()


from generalgui.app import App


