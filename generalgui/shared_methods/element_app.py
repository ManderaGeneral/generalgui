"""Shared methods by Element and App"""

from generallibrary.functions import leadingArgsCount
from generallibrary.iterables import addToListInDict


class Element_App:
    """
    Pure methods that Element and App share.
    """
    def __init__(self):
        self.events = {}
        self.disabledPropagations = []

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

    def _bindCaller(self, event, key):
        """
        Every bound key only has this function bound.

        :param generalgui.Element or generalgui.App self:
        """
        returns = []
        for func in self.events[key]:
            if leadingArgsCount(func):
                value = func(event)
                if value is not None:
                    returns.append(value)
            else:
                value = func()
                if value is not None:
                    returns.append(value)
        if key in self.disabledPropagations:
            return "break"
        return returns

    def createBind(self, key, func, add=True):
        """
        Binds a key to a function using tkinter's bind function.
        Not used directly.

        :param generalgui.Element or generalgui.App self:
        :param str key: A key from https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        :param function or None func: A function to be called or None to unbind
        :param bool add: Add to existing binds instead of overwriting
        :return:
        """
        if func is None or not add:
            self.widget.unbind(key)
            if key in self.events:
                del self.events[key]

        if func is not None:
            if key not in self.events:
                self.widget.bind(key, lambda event: self._bindCaller(event, key), add=False)
            addToListInDict(self.events, key, func)

    def _callBind(self, key):
        """
        Calls a binded key's function(s) manually.
        Not used directly.

        :param generalgui.Element or generalgui.App self:
        :param str key: A key from https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        :return: Function's return value or functions' return values in tuple in the order they were binded.
        """
        self._bindCaller(None, key)

        # if key not in self.events:
        #     raise UserWarning(f"Key {key} is not bound to any function.")
        #
        # # Event is None when calling manually
        # results = tuple(func() for func in self.events[key])
        # if len(results) == 1:
        #     return results[0]
        # else:
        #     return results



