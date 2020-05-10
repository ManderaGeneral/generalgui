"""Shared methods by Page and App"""

from generallibrary.types import typeChecker

class Page_App:
    """
    Pure methods that Page and App share.
    """
    def getChildren(self, ignore=None):
        """
        Get children pages and elements that's one step below in hierarchy.

        :param generalgui.page.Page or generalgui.app.App self: Page or App
        :param any ignore: A single child or multiple children to ignore and not call 'hide' method on
        :return: Children elements in list
        :rtype: list[generalgui.element.Element or generalgui.page.Page]
        """
        ignore = _configureIgnore(ignore)
        return [widget.element for widget in self.widget.winfo_children() if widget.element not in ignore]

    def showChildren(self, ignore=None):
        """
        Calls the 'show' method on all children retrieved from the 'getChildren' method.

        :param generalgui.page.Page or generalgui.app.App self: Page or App
        :param any ignore: A single child or multiple children to ignore and not call 'hide' method on
        """
        for child in self.getChildren(ignore=ignore):
            child.show()

    def hideChildren(self, ignore=None):
        """
        Calls the 'hide' method on all children retrieved from the 'getChildren' method.

        :param generalgui.page.Page or generalgui.app.App self: Page or App
        :param any ignore: A single child or multiple children to ignore and not call 'hide' method on
        """
        for child in self.getChildren(ignore=ignore):
            child.hide()

    def removeChildren(self, ignore=None):
        """
        Calls the 'remove' method on all children retrieved from the 'getChildren' method.

        :param generalgui.page.Page or generalgui.app.App self: Page or App
        :param any ignore: A single child or multiple children to ignore and not call 'hide' method on
        """
        for child in self.getChildren(ignore=ignore):
            child.remove()

from generalgui.shared_methods.element_page_app import _configureIgnore
