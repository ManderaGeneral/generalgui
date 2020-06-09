"""
Binder for app and elements.
Could be it's own package and be called Config and ConfigHandler instead.
"""

from generallibrary.functions import leadingArgsCount


class Binder:
    """
    Binder feature for App and Element.
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

    def createBind(self, key, func, add=True, name=None):
        """
        Add a function to a list in dict that is called with _bindCaller().

        :param generalgui.Element or generalgui.App self:
        :param str key: A key from https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        :param function or None func: A function to be called or None to unbind
        :param bool add: Add to existing binds instead of overwriting
        :param str name: Name of bind, if bind with that name exists then it's replaced
        :return: Bind
        """
        if not add:
            self.removeBind(key)
        elif name:
            self.removeBind(key, name=name)

        bind = Bind(self, key, func, name)
        if key not in self.events:
            self.widget.bind(key, lambda event: self._bindCaller(event, key), add=False)
            self.events[key] = []

        self.events[key].append(bind)
        return bind

    def removeBind(self, key, bind=None, name=None):
        """
        Remove a bind from events.

        :param generalgui.Element or generalgui.App self:
        :param key: A key from https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        :param Bind bind: Specific Bind to be removed
        :param str name: Specific Bind with this name to be removed
        """
        if key in self.events:
            if name is not None:
                for bind in self.events[key]:
                    if bind.name == name:
                        self.events[key].remove(bind)
                        break
            elif bind is not None:
                if bind in self.events[key]:
                    self.events[key].remove(bind)
            else:
                del self.events[key]

        if key in self.events and not self.events[key]:
            del self.events[key]

        if key not in self.events:
            self.widget.unbind(key)

    def _bindCaller(self, event, key):
        """
        Every bound key only has this function bound.

        :param generalgui.Element or generalgui.App self:
        :raises AttributeError: If Element or App is removed
        """
        if not self.exists():
            raise AttributeError(f"Cannot call a removed element's or app's bind: {self}")

        returnBreak = event and key in self.disabledPropagations

        # print(key, returnBreak, self.events.get(key, []))

        returns = []
        for bind in self.events.get(key, []):
            if leadingArgsCount(bind.func):
                value = bind(event)
                if value is not None:
                    returns.append(value)
            else:
                value = bind()
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

    def onClick(self, func, add=True):
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

    def onRightClick(self, func, add=True):
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

class Bind:
    """A specific bind that contains a func"""
    def __init__(self, element, key, func, name=None):
        self.element = element
        self.key = key
        self.func = func
        self.name = name

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    # def __repr__(self):
    #     import inspect
    #     return inspect.getsource(self.func)





























