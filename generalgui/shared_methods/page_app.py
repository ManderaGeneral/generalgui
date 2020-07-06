"""Shared methods by Page and App"""

from generalgui.shared_methods.decorators import ignore

from generallibrary.types import hasMethod

from typing import List


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

    def packPart(self, part):
        """
        Pack a part to this Page or Parent.
        Meant to be overridden if needed.

        There's probably a better way to achieve this behaviour where the parent can change how it's childrens' methods behave.
        We could use it for remove as well for example.

        :param generalgui.page.Page or generalgui.app.App self: Page or App
        :param part: Child part
        """
        part.widget.pack(**part.packParameters)

    def getElementByValue(self, value):
        """

        :param generalgui.page.Page or generalgui.app.App self: Page or App
        :param value:
        """
        parts = [self]  # type: List[any]
        while parts:
            part = parts[0]
            partChildren = part.getChildren()
            if partChildren:
                parts.extend(partChildren)

            elif hasMethod(part, "getValue"):
                if part.getValue() == value:
                    return part

            del parts[0]









































