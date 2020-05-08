
from generalgui.page import Page
from generalgui.element import Text, Button
from generallibrary.time import sleep



def onClick(page):

    page.toggle()
    page.app.toggle()
    sleep(1)
    page.app.toggle()





page = Page()
page2 = Page(page.app)

Text(page, "hello")
Text(page2, "there")


Button(page, "button", page2.show)
Button(page2, "button", page.show)


page.show()






