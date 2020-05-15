"""Random testing"""

from generalgui import Page, Button, Entry, LabelCheckbutton

import tkinter as tk


children = [1, 2, 3, 4]

selfIndex = 1

ret = children[0:selfIndex]
ret.extend(children[selfIndex + 1:])

print(ret)
exit()


page = Page()

labelEntry = LabelCheckbutton(page, "Name:")
Button(page, "Click me", lambda: labelEntry.label.setValue(labelEntry.checkbutton.getValue()))


page.show()

