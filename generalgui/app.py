
from tkinter import Tk

# Inherit Page?
class App:
    """
    Container for Tk() object with a lot of convenient features.
    """
    def __init__(self):
        self.widget = Tk()
        self.parentPage = None
        self.mainlooped = False
        self.app = self

    def isShown(self):
        return self.widget.winfo_ismapped()

    def show(self):
        if not self.isShown():
            self.widget.deiconify()

            if not self.mainlooped:
                self.widget.mainloop()
                self.mainlooped = True

    def hide(self):
        if self.isShown():
            self.widget.withdraw()

    def toggle(self):
        if self.isShown():
            self.hide()
        else:
            self.show()
