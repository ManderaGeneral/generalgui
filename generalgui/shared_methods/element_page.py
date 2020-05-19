"""Shared methods by Element and Page"""

from generallibrary.types import typeChecker

from generalgui.shared_methods.decorators import ignore


class Element_Page:
    """
    Pure methods that Element and Page share.
    """
    def pack(self):
        """
        Packs this Element's widget using the packParameters attribute.

        :param generalgui.element.Element or generalgui.Page self: Element or Page
        """
        if typeChecker(self, "Page", error=False):
            if self.topElement is None:
                raise AttributeError("Cannot pack Page without a topElement.")
            self.topElement.pack()

        else:
            if "column" in self.packParameters and "row" in self.packParameters:
                self._grid()
            else:
                self.widget.pack(**self.packParameters)

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
        parentPages = self.getParentPages(includeSelf=True)
        return parentPages[-1]

    @ignore
    def getSiblings(self, ignore=None):
        """
        Get a list of all siblings of this element or page. Doesn't include self.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        :param any ignore: A single child or multiple children to ignore. Is converted to list through decorator.
        :rtype: list[generalgui.element.Element or generalgui.page.Page]
        """
        children = self.parentPage.getChildren(ignore=ignore)

        if self in children:
            selfIndex = children.index(self)
            siblings = children[selfIndex + 1:]
            siblings.extend(children[0:selfIndex])
            return siblings
        else:
            return children

    @ignore
    def showSiblings(self, ignore=None, mainloop=True):
        """
        Calls the 'show' method on all siblings of this Element or Page retrieved from the 'getSiblings' method.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        :param any ignore: A single child or multiple children to ignore. Is converted to list through decorator.
        :param mainloop: Whether to call mainloop or not
        """
        for sibling in self.getSiblings(ignore=ignore):
            sibling.show(mainloop=False)
        if mainloop:
            self.app.mainloop()

    @ignore
    def hideSiblings(self, ignore=None):
        """
        Calls the 'hide' method on all siblings of this Element or Page.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        :param any ignore: A single child or multiple children to ignore. Is converted to list through decorator.
        """
        for sibling in self.getSiblings(ignore=ignore):
            sibling.hide()

    @ignore
    def removeSiblings(self, ignore=None):
        """
        Calls the 'remove' method on all siblings of this Element or Page.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        :param any ignore: A single child or multiple children to ignore. Is converted to list through decorator.
        """
        for sibling in self.getSiblings(ignore=ignore):
            sibling.remove()

    @ignore
    def nextSibling(self, ignore=None):
        """
        Get the next sibling.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        :param any ignore: A single child or multiple children to ignore. Is converted to list through decorator.
        """
        siblings = self.getSiblings(ignore=ignore)
        if siblings:
            return siblings[0]
        else:
            return None

    @ignore
    def previousSibling(self, ignore=None):
        """
        Get the previos sibling.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        :param any ignore: A single child or multiple children to ignore. Is converted to list through decorator.
        """
        siblings = self.getSiblings(ignore=ignore)
        if siblings:
            return siblings[-1]
        else:
            return None

    def show(self, hideSiblings=False, mainloop=True):
        """
        Show this Element or Page if it's not shown. Propagates through all parent pages so they automatically are shown as well if needed.
        Even creates window automatically if it hasn't been created yet.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        :param hideSiblings: Whether to hide siblings or not
        :param mainloop: Whether to call mainloop on App's widget or not
        """
        if hideSiblings:
            self.parentPage.hideChildren()

        for ele_page in self.getParentPages(includeSelf=True):
            if ele_page.isShown():
                break
            ele_page.pack()

        self.app.show(mainloop=mainloop)

    def hide(self):
        """
        Hide this Element or Page if it's packed.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        """
        if self.isPacked:
            self.widget.pack_forget()

    def toggleShow(self, mainloop=True):
        """
        Hides Element or Page if it's packed and shows it if it's not packed.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        :return: Whether it's shown or not after call
        :param mainloop: Whether to call mainloop or not when being shown
        """
        if self.isPacked():
            self.hide()
            return False
        else:
            self.show(mainloop=mainloop)
            return True

