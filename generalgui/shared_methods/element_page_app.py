"""Shared methods by Element, Page and App"""

from generallibrary.types import typeChecker


class Element_Page_App:
    """
    Pure methods that Element, Page and App all share.
    """
    def getBaseWidget(self):
        """
        Get base widget from a part.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        """
        if typeChecker(self, ("App", "Element"), error=False):
            return self.widget
        else:
            if self.baseElement is None:
                return self.parentPage.getBaseWidget()
            else:
                return self.baseElement.widget

    def getTopWidget(self):
        """
        Get top widget from a part.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        """
        if typeChecker(self, ("App", "Element"), error=False):
            return self.widget
        else:
            if self.topElement is None:
                return self.parentPage.getTopWidget()
            else:
                return self.topElement.widget

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

    def widgetConfig(self, **kwargs):
        """
        Configure widget.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        """
        self.getBaseWidget().config(**kwargs)

    def getWidgetConfigs(self):
        """
        Get all the keys we can use in method 'widgetConfig()' as a list.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        """
        return self.getBaseWidget().keys()



