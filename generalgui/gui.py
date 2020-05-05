
import tkinter as tk

class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.pages = []


    def addPage(self, page):
        """
        Add a page to gui without showing it.

        :param page:
        """
        self.pages.append(page)


