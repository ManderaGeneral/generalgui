
from generalgui.page import Page
from generalgui.element import Text, Button
from generallibrary.time import sleep

import random


def createPage(parentPage):
    page = Page(parentPage, removeSiblings=True)
    Text(page, f"hello {random.randint(0, 1000)}")
    Button(page, "button", lambda: createPage(page.parentPage))
    print(len(page.parentPage.getChildren()))
    page.show(hideSiblings=True)

createPage(None)




