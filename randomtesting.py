"""Random testing"""

from generalgui.page import Page
from generalgui.element import Text, Button
from generallibrary.time import sleep



def aktivering(page):
    """
    test

    :param page:
    :return:
    """
    page.app.hide()
    sleep(1)
    page.app.show()

page = Page()
Text(page, "Lisbeth")

Button(page, "Tryck här!", lambda: aktivering(page))


page.show()



# def createPage(parentPage):
#     page = Page(parentPage, removeSiblings=True)
#     Text(page, f"hello {random.randint(0, 1000)}")
#     Button(page, "button", lambda: createPage(page.parentPage))
#     print(len(page.parentPage.getChildren()))
#     page.show(hideSiblings=False)
#
# createPage(None)




