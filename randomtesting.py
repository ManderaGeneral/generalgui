
from generalgui.page import Page
from generalgui.element import Text, Button
from generallibrary.time import sleep



def onClick(page):

    page.toggle()
    page.app.toggle()
    sleep(1)
    page.app.toggle()





page = Page()
page2 = Page(page)

Text(page, "hello")
Text(page2, "there")


Button(page, "button", lambda: onClick(page2))


page.show()






