
from generalgui.page import Page
from generalgui.element import Text, Button
from generalgui.app import App



def onClick(page):
    page2 = Page(page)
    Text(page2, "there")
    page2.show()



page = Page()
Text(page, "hello")
Button(page, "button", lambda page=page: onClick(page))
page.show()






