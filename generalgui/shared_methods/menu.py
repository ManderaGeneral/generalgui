
from generallibrary.types import typeChecker

from generalvector import Vec2


class Menu_Element_Page_App:
    """Keep all menu functionality in this module"""
    def __init__(self):
        self.menuContent = {}

    def menu(self, name, **buttons):
        """
        Define menu for this part.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        :param name:
        """
        self.menuContent[name] = buttons

class Menu_App:
    """
    Todo: Proper structure - App could have a list of pages containig buttons created by any page that should have a menu
        So multiple pages in menu can be shown at once if menu was opened in a subpage where both pages have a menu
    Menu feature for App.
    Shows a menu when right clicking a page that has a menu enabled.
    """
    def __init__(self):
        """
        :param generalgui.app.App self:
        """
        self.menuPage = None
        self.openMenuOnRelease = False

        self.createBind("<Button-1>", self.hideMenu)
        self.createBind("<Button-3>", self.menuButtonDown)
        self.createBind("<ButtonRelease-3>", self.menuButtonUp)

    def menuButtonDown(self, event):
        """
        :param generalgui.app.App self:
        :param event:
        """
        self.openMenuOnRelease = True
        self.hideMenu()

    def menuButtonUp(self, event):
        """
        :param generalgui.app.App self:
        :param event:
        """
        if self.openMenuOnRelease:
            self.createMenu(event)

    def addLine(self):
        """
        :param generalgui.app.App self:
        """
        linePage = self.Page(self.menuPage, fill="x", pack=True, pady=5)
        self.Frame(linePage, width=5, fill="y", side="left")
        self.Frame(linePage, fill="x", side="left", bg="black", expand=True)
        self.Frame(linePage, width=5, fill="y", side="left")

    def createMenu(self, event):
        """
        :param generalgui.app.App self:
        :param event:
        """
        if self.menuPage:
            self.menuPage.remove()
        self.menuPage = self.Page(self, relief="solid", borderwidth=1)

        self.Label(self.menuPage, "Menu", fill="x")
        self.addLine()

        for part in event.widget.element.getParentPages(includeSelf=True):
            for label, buttons in part.menuContent.items():
                self.Label(self.menuPage, label, fill="x")
                for buttonText, buttonFunc in buttons.items():
                    button = self.Button(self.menuPage, buttonText.replace("_", " "), buttonFunc, fill="x")
                    button.createBind("<ButtonRelease-1>", self.hideMenu, name="HideMenu")
        # self.menuPage.pack()
        # print(self.getMouse(event) - Vec2(8, 35))
        self.menuPage.place(self.getMouse(event) - Vec2(8, 35))

    def hideMenu(self):
        """Hide the menu"""
        if self.menuPage:
            self.menuPage.remove()
            self.menuPage = None






















