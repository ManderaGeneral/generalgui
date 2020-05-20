"""Shared methods by Page and App"""

from generalgui.shared_methods.decorators import ignore


class Page_App:
    """
    Pure methods that Page and App share.
    """

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


