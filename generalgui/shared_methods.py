
from generallibrary.types import typeChecker

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

    def hideChildren(self, ignore=None):
        """

        :param generalgui.page.Page or generalgui.app.App self:
        :param ignore:
        :return:
        """
        for child in self.getChildren():
            if child is not ignore:
                child.hide()

    def removeChildren(self):
        """

        :param generalgui.page.Page or generalgui.app.App self:
        :return:
        """
        for child in self.getChildren():
            child.remove()



class Element_Page:
    def getParentPages(self, includeSelf=False):
        """

        :param generalgui.element.Element or generalgui.page.Page self:
        :param includeSelf:
        :return:
        """
        pages = []
        parentPage = self.parentPage
        while True:
            if typeChecker(parentPage, "App", error=False):
                if includeSelf:
                    pages.insert(0, self)
                return pages
            else:
                pages.append(parentPage)
            parentPage = parentPage.parentPage

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

    def getSiblings(self):
        """

        :param generalgui.element.Element or generalgui.page.Page self:
        :return:
        """
        return self.parentPage.getChildren()

    def showSiblings(self):
        """

        :param generalgui.element.Element or generalgui.page.Page self:
        :return:
        """
        self.parentPage.showChildren()

    def hideSiblings(self):
        """

        :param generalgui.element.Element or generalgui.page.Page self:
        :return:
        """
        self.parentPage.hideChildren(ignore=self)

    def pack(self):
        """

        :param generalgui.element.Element or generalgui.page.Page self:
        :return:
        """
        self.widget.pack(side=self.side)

    def show(self, hideSiblings=False):
        """

        :param hideSiblings:
        :param generalgui.element.Element or generalgui.page.Page self:
        :return:
        """
        if hideSiblings:
            self.parentPage.hideChildren()

        if typeChecker(self, "Element", error=False):
            self.pack()

        for ele_page in self.getParentPages(includeSelf=True):
            if ele_page.isShown():
                return
            ele_page.pack()

        self.app.show()

    def hide(self):
        """

        :param generalgui.element.Element or generalgui.page.Page self:
        :return:
        """
        if self.isShown():
            self.widget.pack_forget()
            self.app.widget.update()

    def toggle(self):
        """

        :param generalgui.element.Element or generalgui.page.Page self:
        :return:
        """
        if self.isShown():
            self.hide()
        else:
            self.show()

