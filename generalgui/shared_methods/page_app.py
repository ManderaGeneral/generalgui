"""Shared methods by Page and App"""

from generalgui.shared_methods.decorators import ignore


class Page_App:
    """
    Pure methods that Page and App share.
    """
    @ignore
    def getChildren(self, ignore=None):
        """
        Get children pages and elements that's one step below in hierarchy.

        :param generalgui.page.Page or generalgui.app.App self: Page or App
        :param any ignore: A single child or multiple children to ignore. Is converted to list through decorator.
        :return: Children elements in list
        :rtype: list[generalgui.element.Element or generalgui.page.Page]
        """
        children = []
        for widget in self.getBaseWidget().winfo_children():
            part = widget.element
            if part.parentPage.topElement == part:
                part = part.parentPage
            if widget.element not in ignore and part not in ignore:
                children.append(widget.element)
        return children

    @ignore
    def showChildren(self, ignore=None, mainloop=True):
        """
        Calls the 'show' method on all children retrieved from the 'getChildren' method.

        :param generalgui.page.Page or generalgui.app.App self: Page or App
        :param any ignore: A single child or multiple children to ignore. Is converted to list through decorator.
        :param mainloop: Whether to call mainloop or not
        """
        for child in self.getChildren(ignore=ignore):
            child.show(mainloop=False)
        if mainloop:
            self.app.mainloop()

    @ignore
    def hideChildren(self, ignore=None):
        """
        Calls the 'hide' method on all children retrieved from the 'getChildren' method.

        :param generalgui.page.Page or generalgui.app.App self: Page or App
        :param any ignore: A single child or multiple children to ignore. Is converted to list through decorator.
        """
        for child in self.getChildren(ignore=ignore):
            child.hide()

    @ignore
    def removeChildren(self, ignore=None):
        """
        Calls the 'remove' method on all children retrieved from the 'getChildren' method.

        :param generalgui.page.Page or generalgui.app.App self: Page or App
        :param any ignore: A single child or multiple children to ignore. Is converted to list through decorator.
        """
        for child in self.getChildren(ignore=ignore):
            child.remove()


