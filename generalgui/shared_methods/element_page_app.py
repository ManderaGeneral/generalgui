"""Shared methods by Element, Page and App"""

from generallibrary.types import typeChecker

from generalvector import Vec

from generalgui.shared_methods.decorators import ignore


class Element_Page_App:
    """
    Pure methods that Element, Page and App all share.
    """
    def rainbow(self, reset=False):
        """
        Give every widget and subwidget recursively a random background color.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        :param reset:
        """

        if typeChecker(self, "Element", error=False):
            if reset:
                if self.styleHandler:
                    self.styleHandler.disable("Rainbow")
            else:
                self.createStyle("Rainbow", priority=0.1, bg=Vec.random(50, 255).hex()).enable()

        for element in self.getChildren(includeParts=True):
            element.rainbow(reset=reset)

    @ignore
    def getChildren(self, includeParts=False, ignore=None):
        """
        Get children pages and elements that's one step below in hierarchy.

        :param generalgui.page.Page or generalgui.app.App self: Page or App
        :param includeParts: Whether to get page parts or one page
        :param any ignore: A single child or multiple children to ignore. Is converted to list through decorator.
        :return: Children elements in list
        :rtype: list[generalgui.element.Element or generalgui.page.Page]
        """
        children = []

        if includeParts:
            for widget in self.getTopWidget().winfo_children():
                if getattr(widget, "element", None) is None:
                    continue

                part = widget.element
                if part not in ignore:
                    children.append(part)

        else:
            for widget in self.getBaseWidget().winfo_children():
                if getattr(widget, "element", None) is None:
                    continue

                part = widget.element
                if part.parentPage.topElement == part:
                    part = part.parentPage

                if widget.element not in ignore and part not in ignore:
                    children.append(part)

        return children

    def getBaseElement(self):
        """
        Get base element from a part.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        :rtype: generalgui.element.Element
        """
        if typeChecker(self, ("App", "Element"), error=False):
            return self
        else:
            if self.baseElement is None:
                return self.parentPage.getBaseElement()
            else:
                return self.baseElement

    def getBaseWidget(self):
        """
        Get base widget from a part.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        """
        return self.getBaseElement().widget

    def getTopElement(self):
        """
        Get top element from a part.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        :rtype: generalgui.element.Element
        """
        if typeChecker(self, ("App", "Element"), error=False):
            return self
        else:
            if self.topElement is None:
                return self.parentPage.getBaseElement()
            else:
                return self.topElement

    def getTopWidget(self):
        """
        Get top widget from a part.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        """
        return self.getTopElement().widget

    def isShown(self):
        """
        Get whether an element's widget is shown or not.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        :rtype: bool
        """
        return not not self.getTopWidget().winfo_ismapped()

    def isPacked(self):
        """
        Get whether an element's widget is packed or not.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        :rtype: bool
        """
        return self.getTopWidget().winfo_manager() != ""

    def remove(self):
        """
        Remove an element's widget for good.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        """
        self.getTopWidget().update()
        self.getTopWidget().destroy()

        # cls = self.__class__
        # for func in dir(cls):
        #     if func.startswith("cleanup_"):
        #         getattr(cls, func)(self)




