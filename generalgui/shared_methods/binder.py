"""
Binder for app and elements.
Could be it's own package and be called Config and ConfigHandler instead.
"""

from generallibrary.functions import leadingArgsCount
from generallibrary.iterables import appendToDict


class Binder:
    """
    Binder feature for App and Element.
    """
    def __init__(self):
        self.events = {}
        self.disabledPropagations = []

    def cleanup_binder(self):
        Binder.__init__(self)

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

        :param generalgui.Element or generalgui.App self:
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
        returnBreak = event and key in self.disabledPropagations

        returns = []
        if key not in self.events:
            if returnBreak:
                return "break"
            else:
                return returns

        for index, func in self.events[key].items():
            if leadingArgsCount(func):
                value = func(event)
                if value is not None:
                    returns.append(value)
            else:
                value = func()
                if value is not None:
                    returns.append(value)

        if returnBreak:
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

    def onClick(self, func, add=False):
        """
        Call a function when this element is left clicked.

        :param generalgui.Element or generalgui.App self:
        :param function or None func: Any function or None to unbind
        :param add: Whether to add to functions list or replace all
        """
        self.createBind(key="<Button-1>", func=func, add=add)

    def click(self, animate=True):
        """
        Manually call the function that is called when this element is left clicked.

        :param generalgui.Element or generalgui.App self:
        :param animate: Whether to animate or not
        """
        value = self.callBind("<Button-1>")

        if animate:
            self.widget.after(250, lambda: self.callBind("<ButtonRelease-1>"))
        else:
            self.callBind("<ButtonRelease-1>")

        return value

    def onRightClick(self, func, add=False):
        """
        Call a function when this element is right clicked.

        :param generalgui.Element or generalgui.App self:
        :param function or None func: Any function or None to unbind
        :param add: Whether to add to functions list or replace all
        """
        self.createBind(key="<Button-3>", func=func, add=add)

    def rightClick(self, animate=True):
        """
        Manually call the function that is called when this element is right clicked.

        :param generalgui.Element or generalgui.App self:
        :param animate: Whether to animate or not
        """
        value = self.callBind("<Button-3>")

        if animate:
            self.widget.after(250, lambda: self.callBind("<ButtonRelease-3>"))
        else:
            self.callBind("<Button-3>")

        return value
