"""
Binder for app and elements.
Could be it's own package and be called Config and ConfigHandler instead.
"""

from generallibrary.functions import leadingArgsCount
from generallibrary.iterables import addToListInDict, uniqueObjInList
from generallibrary.types import typeChecker


class Binder_App:
    """Binder feature for App"""
    def __init__(self):
        """

        :param generalgui.App self:
        """
        self.boundKeys = []

    def widgetBind(self, key):
        """
        Do a non-reversible one-time bind to app's Tk widget.
        Since all binds are stored in each part, it's nice if App doesn't have to keep track of them.
        Therefore all App has to do is bind the key, even if the part that caused the bind unbinds it.

        :param generalgui.App self:
        :param str key:
        """
        if key not in self.boundKeys:
            self.widget.bind(key, lambda event: self.bindCaller(event, key), add=False)
            self.boundKeys.append(key)

    def bindCaller(self, event_or_element, key):
        """
        This method is bound to App's widget for any part key that is bound.
        It starts with event.widget.element and goes through all parents to call each method stored in self.events.
        It stops if it reaches App or a disabled propagation.

        :param generalgui.App self:
        :param any event_or_element:
        :param str key:
        """
        if not self.exists():
            return []

        if typeChecker(event_or_element, "Element", error=False):
            element = event_or_element
            event = None
        else:
            element = getattr(event_or_element.widget, "element", None)
            if element is None:
                return
            event = event_or_element
        if not element.exists():
            return []

        returns = []
        for part in element.getParents(includeSelf=True, includeApp=True):
            for bind in part.events.get(key, []):
                if leadingArgsCount(bind.func):
                    value = bind(event)
                else:
                    value = bind()

                if value is not None:
                    returns.append(value)

            if key in part.disabledPropagations:
                break
        return returns

class Binder:
    """Binder feature for all parts"""
    def __init__(self):
        self.events = {}
        self.disabledPropagations = []

    def setBindPropagation(self, key, enable):
        """
        Enabled or disable propagation for binds.
        Can be used to disable click animations on buttons for example.
        Make the last function called with this bind return "break" which tkinter listens to.
        All propagations are enabled by default.

        :param generalgui.Element or generalgui.Page or generalgui.App self:
        :param str key: Bind key, <Button-1> for example.
        :param bool enable: Whether to enable propagation or not.
        """
        uniqueObjInList(self.disabledPropagations, key, not enable)

    def createBind(self, key, func, add=True, name=None):
        """
        Add a function to a list in dict that is called with _bindCaller().
        If a bind exists with same name and key then it's overwritten.

        :param generalgui.Element or generalgui.Page or generalgui.App self:
        :param str key: A key from https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        :param function or None func: A function to be called or None to unbind
        :param bool add: Add to existing binds instead of overwriting
        :param str name: Name of bind, if bind with that name exists then it's replaced
        :return: Bind
        :raises NameError: If bind name exists with another key
        """
        if not add:
            self.removeBind(key)
        elif name:
            existingBind = self.getBindByName(name)
            if existingBind:
                if existingBind.key == key:
                    existingBind.remove()
                else:
                    raise NameError(f"{existingBind} is already using this name with another key")

        bind = Bind(element=self, key=key, func=func, name=name)
        addToListInDict(self.events, key, bind)
        self.app.widgetBind(key)

        # print(typeChecker(self, "Element", error=False), key == "<Button-1>", self.styleHandler)

        if typeChecker(self, "Element", error=False) and key == "<Button-1>" and (not self.styleHandler or "Hover" not in self.styleHandler.allStyles):
            self.widgetConfig(cursor="hand2")
            self.createStyle("Hover", "<Enter>", "<Leave>", bg="gray90")
            self.createStyle("Click", "<Button-1>", "<ButtonRelease-1>", style="Hover", relief="sunken", fg="gray40")
            self.createBind("<Return>", self.click)

        return bind

    def getBindByName(self, name):
        """
        Get a bind by name.

        :param str name: Name of bind
        :rtype: Bind
        """
        if name is None:
            raise NameError("Cannot get bind by name None")

        for key, binds in self.events.items():
            for bind in binds:
                if bind.name == name:
                    return bind

    def removeBind(self, key, bind=None, name=None):
        """
        Remove a bind by key or bind object or name.

        :param generalgui.Element or generalgui.Page or generalgui.App self:
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

    def callBind(self, key):
        """
        Calls a binded key's function(s) manually.

        :param generalgui.Element or generalgui.Page or generalgui.App self:
        :param str key: A key from https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        :return: Function's return value or functions' return values in tuple in the order they were binded.
        """
        return self.app.bindCaller(self, key)

    def onClick(self, func, add=True):
        """
        Call a function when this element is left clicked.

        :param generalgui.Element or generalgui.Page or generalgui.App self:
        :param function or None func: Any function or None to unbind
        :param add: Whether to add to functions list or replace all
        """
        self.createBind(key="<Button-1>", func=func, add=add)

    def click(self, animate=True):
        """
        Manually call the function that is called when this element is left clicked.

        :param generalgui.Element or generalgui.Page or generalgui.App self:
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

        :param generalgui.Element or generalgui.Page or generalgui.App self:
        :param function or None func: Any function or None to unbind
        :param add: Whether to add to functions list or replace all
        """
        self.createBind(key="<Button-3>", func=func, add=add)

    def rightClick(self, animate=True):
        """
        Manually call the function that is called when this element is right clicked.

        :param generalgui.Element or generalgui.Page or generalgui.App self:
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
        self.name = name
        self.key = key
        self.func = func

    def __repr__(self):
        return f"<Bind - Name: {self.name} - Key: {self.key}>"

    def __call__(self, *args, **kwargs):
        if not self.element.removed:
            return self.func(*args, **kwargs)

    def remove(self):
        """Remove this bind from it's element"""
        self.element.removeBind(key=self.key, bind=self)

    # def __repr__(self):
    #     import inspect
    #     return inspect.getsource(self.func)





























