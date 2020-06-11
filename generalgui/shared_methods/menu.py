

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
    Menu should probably inherit page so it becomes reuseable

    Menu feature for App.
    Shows a menu when right clicking a page that has a menu enabled.
    """
    def __init__(self):
        """
        :param generalgui.app.App self:
        """
        self.menuPage = None
        self.openMenuOnRelease = False
        self.menuTargetElement = None

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
        linePage = self.Page(self.menuPage, fill="x", pack=True, pady=10)
        self.Frame(linePage, fill="x", bg="gray")
        self.Frame(linePage, fill="x", height=2)
        self.Frame(linePage, fill="x", bg="gray")

    def addLabel(self, text):
        """
        :param generalgui.app.App self:
        :param text:
        """
        self.Label(self.menuPage, text, fill="x")

    def addButton(self, text, func):
        """
        :param generalgui.app.App self:
        :param text:
        :param func:
        """
        button = self.Button(self.menuPage, text.replace("_", " "), func, fill="x")
        button.createBind("<ButtonRelease-1>", self.hideMenu, name="HideMenu")

    def createMenu(self, event):
        """
        :param generalgui.app.App self:
        :param event:
        """
        self.menuTargetElement = event.widget.element
        if self.menuPage:
            self.menuPage.remove()

        self.menuPage = self.Page(self, relief="solid", borderwidth=1, padx=5, pady=5)
        for part in event.widget.element.getParentPages(includeSelf=True, includeApp=True):
            if part.menuContent:
                self.addLine()
            for label, buttons in part.menuContent.items():
                self.addLabel(label)
                for buttonText, buttonFunc in buttons.items():
                    if buttonText.endswith(":"):
                        buttonValue = buttonFunc()
                        if buttonValue is not None:
                            self.addLabel(f"{buttonText} {buttonValue}")
                    else:
                        self.addButton(buttonText, buttonFunc)

        self.menuPage.place(self.getMouse())

    def hideMenu(self):
        """Hide the menu"""
        if self.menuPage:
            self.menuPage.remove()
            self.menuPage = None
            self.menuTargetElement = None






















