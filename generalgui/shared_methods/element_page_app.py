"""Shared methods by Element, Page and App"""

import tkinter as tk

from generallibrary.types import typeChecker

from generalvector import Vec, Vec2

from generalgui.shared_methods.decorators import ignore

from generalgui.shared_methods.menu import Menu_Element_Page_App


class Element_Page_App(Menu_Element_Page_App):
    """
    Pure methods that Element, Page and App all share.
    """
    def __init__(self):
        Menu_Element_Page_App.__init__(self)

    def getWindowPos(self):
        """
        Get current window position of the upper left corner.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        """
        return Vec2(self.app.widget.winfo_rootx(), self.app.widget.winfo_rooty())

    def getTopLeftPos(self):
        """
        Get top left corner of this part's widget.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        """
        return Vec2(self.getTopWidget().winfo_rootx(), self.getTopWidget().winfo_rooty()) - self.getWindowPos()

    def getBottomRightPos(self):
        """
        Get bottom right corner of this part's widget.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        """
        return self.getTopLeftPos() + self.getSize()

    def getSize(self):
        """
        Get size of this part's widget.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        """
        return Vec2(self.getTopWidget().winfo_width(), self.getTopWidget().winfo_height())

    def getMouse(self):
        """
        Get mouse vector2 from event, can be any part in whole app.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        """
        return Vec2(self.app.widget.winfo_pointerx(), self.app.widget.winfo_pointery()) - self.getWindowPos()

    def getElementByPos(self, pos=None):
        """
        Get element from pos

        :param Vec2 or float pos: Pixel pos to search for element, defaults to getMouse().
        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        """
        if pos is None:
            pos = self.getMouse()
        else:
            pos = Vec2(pos)
        pos += self.getWindowPos()
        widget = self.app.widget.winfo_containing(pos.x, pos.y)

        return getattr(widget, "element", None)

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

    def getParentPages(self, includeSelf=False, includeApp=False):
        """
        Retrieves parent pages from element or page going all the way up to a top page that has App as it's 'parentPage' attribute.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        :param includeSelf: Whether to include self or not (Element or Page) as index 0
        :param includeApp: Whether to include app or not
        :rtype: list[generalgui.element.Element or generalgui.page.Page]
        """
        pages = []

        if typeChecker(self, "App", error=False):
            if includeApp or includeSelf:
                return [self]
            else:
                return []

        parentPage = self.parentPage
        while True:
            if typeChecker(parentPage, "App", error=False):
                if includeSelf:
                    pages.insert(0, self)
                if includeApp:
                    pages.append(parentPage)
                return pages
            else:
                pages.append(parentPage)
            parentPage = parentPage.parentPage

    def getFirstParentClass(self, className, includeSelf=False):
        """
        Iterate parent pages to return first className match.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        :param className: Name or type of part, used by typeChecker
        :param includeSelf:
        """
        for part in self.getParentPages(includeSelf=includeSelf):
            if typeChecker(part, className, error=False):
                return part

    @ignore
    def getChildren(self, includeParts=False, ignore=None):
        """
        Get children pages and elements that's one step below in hierarchy.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        :param includeParts: Whether to get page parts or one page
        :param any ignore: A single child or multiple children to ignore. Is converted to list through decorator.
        :return: Children elements in list
        :rtype: list[generalgui.element.Element or generalgui.page.Page]
        """
        children = []

        parentWidget = self.getTopWidget() if includeParts else self.getBaseWidget()

        for widget in parentWidget.winfo_children():
            if getattr(widget, "element", None) is None:
                continue
            part = widget.element

            if not includeParts and part.parentPage.topElement == part:
                part = part.parentPage

            if widget.element not in ignore and part not in ignore:
                children.append(part)

        return children

    def getBaseElement(self):
        """
        Get base element from a part.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        :rtype: generalgui.element.Element or generalgui.Frame
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
        :rtype: generalgui.element.Element or generalgui.Frame
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

    def isShown(self, error=True):
        """
        Get whether an element's widget is shown or not.
        Error only occurs if widget doesn't exist!

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        :param error: Whether to raise error if widget is destroyed or not
        """
        try:
            isMapped = not not self.getTopWidget().winfo_ismapped()
        except tk.TclError as e:
            if error:
                raise e
            else:
                return False
        return isMapped

    def exists(self):
        """
        Get whether an element's widget is shown or not.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        """
        return not not self.getTopWidget().winfo_exists()

    def isPacked(self):
        """
        Get whether an element's widget is packed or not.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        """
        return self.getTopWidget().winfo_manager() != ""

    def remove(self):
        """
        Remove an element's widget for good.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        """
        if typeChecker(self, "App", error=False):
            self.getApps().remove(self)
            # self.widget.update()
            self.widget.quit()
        else:
            self.getTopWidget().update()
            self.getTopWidget().destroy()





