"""Shared methods by Element and App"""


from generalgui.shared_methods.styler import Styler
from generalgui.shared_methods.binder import Binder

class Element_App(Styler, Binder):
    """
    Pure methods that Element and App share.
    """
    def __init__(self):
        Styler.__init__(self)
        Binder.__init__(self)

    def widgetConfig(self, **kwargs):
        """
        Configure widget.

        :param generalgui.Element or generalgui.App self:
        """
        self.widget.config(**kwargs)

    def getAllWidgetConfigs(self):
        """
        Get all the keys we can use in method 'widgetConfig()' as a list.

        :param generalgui.Element or generalgui.App self:
        """
        return self.widget.keys()

    def getWidgetConfig(self, key):
        """
        Get a current config value on the widget.

        :param generalgui.Element or generalgui.App self:
        :param str key:
        """
        return self.widget[key]


