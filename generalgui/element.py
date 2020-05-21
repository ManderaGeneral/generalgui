"""Element for generalgui, controls a widget that's not App or Page"""

import inspect

import tkinter as tk

from generallibrary.functions import leadingArgsCount, getSignatureNames
from generallibrary.iterables import addToListInDict
from generallibrary.types import typeChecker

from generalgui.shared_methods.element_page import Element_Page
from generalgui.shared_methods.element_page_app import Element_Page_App
from generalgui.shared_methods.styler import StyleHandler, Style


class Element(Element_Page, Element_Page_App):
    """
    Element is inherited by all tkinter widgets exluding App and Page.
    Shown by default. So when it's page is shown then all of page's children are shown automatically.
    """
    def __init__(self, parentPage, widgetClass, pack=True, makeBase=False, **parameters):
        typeChecker(parentPage, "Page")

        parameters["master"] = parentPage.getBaseWidget()

        initArgs = []
        signature = inspect.signature(widgetClass)

        for parameterName in signature.parameters:
            parameter = signature.parameters[parameterName]
            kind = str(parameter.kind)
            if kind == "VAR_KEYWORD":
                break
            if parameterName in parameters:
                if kind == "VAR_POSITIONAL":
                    initArgs.extend(parameters[parameterName])
                else:
                    initArgs.append(parameters[parameterName])
                del parameters[parameterName]
            elif parameter.default != inspect.Parameter.empty:
                initArgs.append(parameter.default)
            elif kind == "VAR_POSITIONAL":
                break
            else:
                raise AttributeError(f"Missing positional parameter that doesn't have a default value {parameterName} with kind {kind}")

        self.widget = widgetClass(*initArgs)

        setattr(self.widget, "element", self)
        self.parentPage = parentPage
        self.parentPart = parentPage if parentPage.baseElement is None else parentPage.baseElement
        self.app = parentPage.app
        self.events = {}
        self.styleHandler = None

        configParameters = {}
        self.packParameters = {}
        allConfigKeys = self.getAllWidgetConfigs()
        for key, value in parameters.items():
            if key in allConfigKeys:
                configParameters[key] = value
            else:
                self.packParameters[key] = value
        self.widgetConfig(**configParameters)

        if makeBase:
            self.makeBase()
        if pack:
            self.pack()

    def makeBase(self):
        self.parentPage.baseElement = self
        if self.parentPage.topElement is None:
            self.parentPage.topElement = self

    def _grid(self):
        self.widget.grid(**self.packParameters)

    def createBind(self, key, func, add=False):
        """
        Binds a key to a function using tkinter's bind function.
        Not used directly.

        :param str key: A key from https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        :param function or None func: A function to be called or None to unbind
        :param bool add: Add to existing binds instead of overwriting
        :return:
        """
        if func is None:
            self.widget.unbind(key)
            if key in self.events:
                del self.events[key]
        else:
            if leadingArgsCount(func) < 1:
                oldFunc = func
                func = lambda _: oldFunc()

            if add:
                addToListInDict(self.events, key, func)
            else:
                self.events[key] = [func]
            self.widget.bind(key, func, add=add)

    def _callBind(self, key):
        """
        Calls a binded key's function(s) manually.
        Not used directly.

        :param str key: A key from https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        :return: Function's return value or functions' return values in tuple in the order they were binded.
        """
        if key not in self.events:
            raise UserWarning(f"Key {key} is not bound to any function.")

        # Event is None when calling manually
        results = tuple(func(None) for func in self.events[key])
        if len(results) == 1:
            return results[0]
        else:
            return results

    def onClick(self, func, add=False):
        """
        Call a function when this element is left clicked.

        :param function or None func: Any function or None to unbind
        :param add: Whether to add to functions list or replace all
        """
        self.createBind(key="<Button-1>", func=func, add=add)
    def click(self):
        """Manually call the function that is called when this element is left clicked."""
        return self._callBind("<Button-1>")

    def onRightClick(self, func, add=False):
        """
        Call a function when this element is right clicked.

        :param function or None func: Any function or None to unbind
        :param add: Whether to add to functions list or replace all
        """
        self.createBind(key="<Button-3>", func=func, add=add)

    def rightClick(self):
        """Manually call the function that is called when this element is right clicked."""
        return self._callBind("<Button-3>")


    def widgetConfig(self, **kwargs):
        """
        Configure widget.
        """
        self.widget.config(**kwargs)

    def getAllWidgetConfigs(self):
        """
        Get all the keys we can use in method 'widgetConfig()' as a list.
        """
        return self.widget.keys()

    def getWidgetConfig(self, key):
        """
        Get a current config value on the widget.
        """
        return self.widget[key]

    def createStyle(self, name, hook=None, unhook=None, priority=None, **kwargs):
        """
        Create a new style and automatically add it to this StyleHandler.

        :param str name: Name of new style
        :param str hook: Bind this element with this key to enable this style.
        :param str unhook: Bind this element with this key to disable this style.
        :param float priority: Priority value, originalStyle has priority 0. If left as None then it becomes highestPriority + 1.
        :param kwargs: Keys and values for new style.
        """
        if self.styleHandler is None:
            self.styleHandler = StyleHandler(lambda kwargs: self.widgetConfig(**kwargs), lambda key: self.getWidgetConfig(key))

        style = self.styleHandler.createStyle(name=name, priority=priority, **kwargs)

        if hook:
            self.createBind(key=hook, func=style.enable, add=True)
        if unhook:
            self.createBind(key=unhook, func=style.disable, add=True)

        return style






























