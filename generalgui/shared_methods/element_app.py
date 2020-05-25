"""Shared methods by Element and App"""

from generallibrary.functions import leadingArgsCount
from generallibrary.iterables import appendToDict

from generalgui.shared_methods.styler import StyleHandler


class Element_App:
    """
    Pure methods that Element and App share.
    """
    def __init__(self):
        self.events = {}
        self.disabledPropagations = []
        self.styleHandler = None

    def setBindPropagation(self, key, enable):
        """
        Enabled or disable propagation for binds.
        Can be used to disable click animations on buttons for example.
        Make the last function called with this bind return "break" which tkinter listens to.
        All propagations are enabled by default.

        :param generalgui.Element or generalgui.App self:
        :param str key: Bind key, <Button-1> for example.
        :param bool enable: Whether to enable propagation or not.
        """
        if enable:
            if key in self.disabledPropagations:
                self.disabledPropagations.remove(key)
        else:
            if key not in self.disabledPropagations:
                self.disabledPropagations.append(key)

    def createBind(self, key, func, add=True):
        """
        Add a function to a dict that is called with _bindCaller().
        If None is passed as func then key gets unbinded.

        :param generalgui.Element or generalgui.App self:
        :param str key: A key from https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        :param function or None func: A function to be called or None to unbind
        :param bool add: Add to existing binds instead of overwriting
        :return: Bind index
        """
        if func is None or not add:
            self.widget.unbind(key)
            if key in self.events:
                del self.events[key]
                self.widget.unbind(key)

        if func is not None:
            if key not in self.events:
                self.widget.bind(key, lambda event: self._bindCaller(event, key), add=False)
                self.events[key] = {}
            return appendToDict(self.events[key], func)

    def removeBind(self, key, bindIndex):
        """
        Remove a bind from events.

        :param key: A key from https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        :param bindIndex: Bind index returned from createBind()
        """
        if key in self.events and bindIndex in self.events[key]:
            del self.events[key][bindIndex]
            if not len(self.events[key]):
                del self.events[key]

    def _bindCaller(self, event, key):
        """
        Every bound key only has this function bound.

        :param generalgui.Element or generalgui.App self:
        """
        if key not in self.events:
            return None

        returns = []
        for index, func in self.events[key].items():
            if leadingArgsCount(func):
                value = func(event)
                if value is not None:
                    returns.append(value)
            else:
                value = func()
                if value is not None:
                    returns.append(value)
        if event and key in self.disabledPropagations:
            return "break"
        return returns

    def callBind(self, key):
        """
        Calls a binded key's function(s) manually.

        :param generalgui.Element or generalgui.App self:
        :param str key: A key from https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        :return: Function's return value or functions' return values in tuple in the order they were binded.
        """
        return self._bindCaller(None, key)

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

    def createStyle(self, name, hookBindKey=None, unhookBindKey=None, style=None, priority=None, **kwargs):
        """
        Create a new style and automatically add it to this StyleHandler.
        If hooks aren't used then you need to call enable and disable on the style object that's returned.

        :param str name: Name of new style
        :param str hookBindKey: Bind this element with this key to enable this style.
        :param str unhookBindKey: Bind this element with this key to disable this style.
        :param str or style style: Optional Style to inherit kwargs from.
        :param float priority: Priority value, originalStyle has priority 0. If left as None then it becomes highestPriority + 1.
        :param kwargs: Keys and values for new style. [prefix][styleName] to copy another style's value at the time of update.
        """

        if self.styleHandler is None:
            self.styleHandler = StyleHandler(lambda kwargs: self.widgetConfig(**kwargs), lambda key: self.getWidgetConfig(key))

        newStyle = self.styleHandler.createStyle(name=name, style=style, priority=priority, **kwargs)

        if hookBindKey:
            self.createBind(key=hookBindKey, func=newStyle.enable, add=False)
        if unhookBindKey:
            self.createBind(key=unhookBindKey, func=newStyle.disable, add=False)

        return newStyle
