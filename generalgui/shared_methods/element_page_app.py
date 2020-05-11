"""Shared methods by Element, Page and App"""

class Element_Page_App:
    """
    Pure methods that Element, Page and App all share.
    """
    def isShown(self):
        """
        Get whether an element's widget is shown or not.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        :rtype: bool
        """
        return self.widget.winfo_ismapped()

    def isPacked(self):
        """
        Get whether an element's widget is packed or not.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        :rtype: bool
        """
        return self.widget.winfo_manager() != ""

    def remove(self):
        """
        Remove an element's widget for good.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element, Page or App
        """
        self.widget.destroy()


