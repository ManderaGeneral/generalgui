"""Shared methods by Element and Page"""

from generallibrary.types import typeChecker

class Element_Page:
    """
    Pure methods that Element and Page share.
    """
    def getParentPages(self, includeSelf=False):
        """
        Retrieves parent pages from element or page going all the way up to a top page that has App as it's 'parentPage' attribute.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        :param includeSelf: Whether to include self or not (Element or Page) as index 0
        :rtype: list[generalgui.element.Element or generalgui.page.Page]
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
        Get the top page that has it's App as it's 'parentPage' attribute and has this element or page as a descendant.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        :rtype: generalgui.page.Page
        """
        parentPages = self.getParentPages()
        if parentPages:
            topPage = parentPages[-1]
        else:
            topPage = self
        return topPage

    def getSiblings(self, ignore=None):
        """
        Get a list of all siblings of this element or page. Doesn't include self.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        :param any ignore: A single child or multiple children to ignore and not call 'hide' method on
        :rtype: list[generalgui.element.Element or generalgui.page.Page]
        """
        ignore = _configureIgnore(ignore)
        ignore.append(self)
        return self.parentPage.getChildren(ignore=ignore)

    def showSiblings(self, ignore=None):
        """
        Calls the 'show' method on all siblings of this Element or Page retrieved from the 'getSiblings' method.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        :param any ignore: A single child or multiple children to ignore and not call 'hide' method on
        """
        for sibling in self.getSiblings(ignore=ignore):
            sibling.show()

    def hideSiblings(self, ignore=None):
        """
        Calls the 'hide' method on all siblings of this Element or Page.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        :param any ignore: A single child or multiple children to ignore and not call 'hide' method on
        """
        for sibling in self.getSiblings(ignore=ignore):
            sibling.hide()

    def removeSiblings(self, ignore=None):
        """
        Calls the 'remove' method on all siblings of this Element or Page.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        :param any ignore: A single child or multiple children to ignore and not call 'hide' method on
        """
        for sibling in self.getSiblings(ignore=ignore):
            sibling.remove()

    def pack(self):
        """
        Should not have to be called manually.
        Packs this Element or Page using it's 'side' attribute.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        """
        self.widget.pack(side=self.side)

    def show(self, hideSiblings=False):
        """
        Show this Element or Page if it's not shown. Propagates through all parent pages so they automatically are shown as well if needed.
        Even creates window automatically if it hasn't been created yet.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        :param hideSiblings: Whether to hide siblings or not
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
        Hide this Element or Page if it's shown.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        """
        if self.isShown():
            self.widget.pack_forget()
            self.app.widget.update()  # Because if sleep(1) was called directly after for example then the window locked and did nothing.

    def toggle(self):
        """
        Hides Element or Page if it's shown and shows it if it's not shown.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        :return: Whether it's shown or not after call
        """
        if self.isShown():
            self.hide()
            return False
        else:
            self.show()
            return True

from generalgui.shared_methods.element_page_app import _configureIgnore
