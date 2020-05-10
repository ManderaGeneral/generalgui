"""Random testing"""

from generalgui.app import App
from generalgui.page import Page
from generalgui.element import Text, Button
from generallibrary.time import sleep





app = App()

page = Page(app)
Text(page, "hello")

page2 = Page(app)
Text(page2, "there")

app.showChildren(ignore=page, mainloop=False)
app.hideChildren()
app.showChildren(mainloop=False)
# app.widget.update()


print(page.isShown())
print(page2.isShown())


