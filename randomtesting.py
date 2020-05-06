
from generalgui.page import Page
from generalgui.element import Text
from generalgui.app import App




page = Page()
Text(page, "hello")

page2 = Page(page)
Text(page2, "there")
page2.show()


