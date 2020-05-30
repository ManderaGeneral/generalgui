
from generallibrary.types import typeChecker

from generalvector import Vec2


class Menu:
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
        self.menu = None
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
            self.menu.place(self.getMouse(event) - Vec2(8, 35))

            # HERE ** Prototype - Do this when creating buttons instead
            for element in self.menu.getChildren():
                if typeChecker(element, "Button", error=False):
                    element.createBind("<ButtonRelease-1>", self.hideMenu, name="HideMenu")

    def hideMenu(self):
        """Hide the menu"""
        self.menu.getTopElement().widget.place_forget()
