
from generallibrary.types import typeChecker

class Element_Page:
    def getParentPages(self, includeSelf=False):
        """

        :param generalgui.element.Element or generalgui.page.Page self:
        :param includeSelf:
        :return:
        """
        pages = [self]
        while True:
            parentPage = pages[-1].parentPage
            if typeChecker(parentPage, "App"):
                if includeSelf:
                    return pages
                else:
                    return pages[1:]
            else:
                pages.append(parentPage)

    def getTopPage(self):
        """

        :param generalgui.element.Element or generalgui.page.Page self:
        :return:
        """
        parentPages = self.getParentPages()
        if parentPages:
            topPage = parentPages[-1]
        else:
            topPage = self
        return topPage

    def toggle(self):
        """

        :param generalgui.element.Element or generalgui.page.Page self:
        :return:
        """
        if self.isShown():
            self.hide()
        else:
            self.show()

class Page_App:

    def getChildren(self):
        """

        :param generalgui.page.Page or generalgui.app.App self:
        :return:
        """
        return [widget.element for widget in self.widget.winfo_children()]

    def showChildren(self):
        """

        :param generalgui.page.Page or generalgui.app.App self:
        :return:
        """
        for child in self.getChildren():
            child.show()

    def hideChildren(self):
        """

        :param generalgui.page.Page or generalgui.app.App self:
        :return:
        """
        for child in self.getChildren():
            child.hide()

    def removeChildren(self):
        """

        :param generalgui.page.Page or generalgui.app.App self:
        :return:
        """
        for child in self.getChildren():
            child.remove()

class Element_Page_App:
    def isShown(self):
        """
        :param generalgui.element.Element or generalgui.page.Page self:
        """
        return self.widget.winfo_ismapped()

    def remove(self):
        """

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self:
        :return:
        """
        self.widget.destroy()

