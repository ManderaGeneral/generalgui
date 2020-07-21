"""Shared methods by Page and App"""

from generalgui.shared_methods.decorators import ignore

from generallibrary.types import hasMethod, typeChecker

from typing import List, Any


class Page_App:
    """
    Pure methods that Page and App share.
    """

    @ignore
    def showChildren(self, ignore=None, recurrent=False, mainloop=True):
        """
        Calls the 'show' method on all children retrieved from the 'getChildren' method.

        :param generalgui.page.Page or generalgui.app.App self: Page or App
        :param any ignore: A single child or multiple children to ignore. Is converted to list through decorator.
        :param recurrent: Whether to include childrens' children or not
        :param mainloop: Whether to call mainloop or not
        """
        for child in self.getChildren(ignore=ignore, recurrent=recurrent):
            child.show(mainloop=False)
        if mainloop:
            self.app.mainloop()

    @ignore
    def hideChildren(self, recurrent=False, ignore=None):
        """
        Calls the 'hide' method on all children retrieved from the 'getChildren' method.

        :param generalgui.page.Page or generalgui.app.App self: Page or App
        :param any ignore: A single child or multiple children to ignore. Is converted to list through decorator.
        :param recurrent: Whether to include childrens' children or not
        """
        for child in self.getChildren(ignore=ignore, recurrent=recurrent):
            child.hide()

    @ignore
    def removeChildren(self, recurrent=False, ignore=None):
        """
        Calls the 'remove' method on all children retrieved from the 'getChildren' method.

        :param generalgui.page.Page or generalgui.app.App self: Page or App
        :param any ignore: A single child or multiple children to ignore. Is converted to list through decorator.
        :param recurrent: Whether to include childrens' children or not
        """
        for child in self.getChildren(ignore=ignore, recurrent=recurrent):
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
        Get the first found element with a value.
        Searches childrens' children etc.
        Tries calling 'getValue()' on parts.

        :param generalgui.page.Page or generalgui.app.App self: Page or App
        :param value:
        """
        parts = [self]  # type: List[Any]
        while parts:
            part = parts[0]
            partChildren = part.getChildren()
            if partChildren:
                parts.extend(partChildren)

            elif hasMethod(part, "getValue"):
                if part.getValue() == value:
                    return part

            del parts[0]

    def maximize(self):
        """
        Maximize this page or app.
        Pages' size are just set to 10000 because tkinter seems to handle it nicely.

        :param generalgui.page.Page or generalgui.app.App self: Page or App
        :return:
        """
        if typeChecker(self, "Page", error=False):
            self.setSize(10000)
        self.app.widget.state("zoomed")









































