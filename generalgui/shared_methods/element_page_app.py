"""Shared methods by Element, Page and App"""

class Element_Page_App:
    """
    Pure methods that Element, Page and App all share.
    """
    def isShown(self):
        """
        Get whether an element's widget is shown or not.

        :param generalgui.element.Element or generalgui.page.Page self: Element or Page
        :rtype: bool
        """
        return self.widget.winfo_ismapped()

    def remove(self):
        """
        Remove an element's widget for good.

        :param generalgui.element.Element or generalgui.page.Page or generalgui.app.App self: Element or Page
        """
        self.widget.destroy()

def _configureIgnore(ignore):
    if not isinstance(ignore, (tuple, list)):
        ignore = [ignore]
    return [value for value in ignore if value is not None]
