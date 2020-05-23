"""Element for generalgui, controls a widget that's not App or Page"""

import inspect

from generallibrary.types import typeChecker
from generallibrary.time import sleep


from generalgui.shared_methods.element_page import Element_Page
from generalgui.shared_methods.element_page_app import Element_Page_App
from generalgui.shared_methods.element_app import Element_App
from generalgui.shared_methods.styler import StyleHandler


class Element(Element_Page, Element_App, Element_Page_App):
    """
    Element is inherited by all tkinter widgets exluding App and Page.
    Shown by default. So when it's page is shown then all of page's children are shown automatically.
    """
    def __init__(self, parentPage, widgetClass, pack=True, makeBase=False, **parameters):
        super().__init__()
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

        self.parameters = parameters
        self.widget = widgetClass(*initArgs)

        setattr(self.widget, "element", self)
        self.parentPage = parentPage
        self.parentPart = parentPage if parentPage.baseElement is None else parentPage.baseElement
        self.app = parentPage.app
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

        self.onClick(lambda: print(self))

        if makeBase:
            self.makeBase()
        if pack:
            self.pack()

    def makeBase(self):
        """
        Make this element the new base to the page it belongs to.
        If page doesn't have a top then this one becomes it as well.
        """
        self.parentPage.baseElement = self
        if self.parentPage.topElement is None:
            self.parentPage.topElement = self

    def _grid(self):
        self.widget.grid(**self.packParameters)

    def onClick(self, func, add=False):
        """
        Call a function when this element is left clicked.

        :param function or None func: Any function or None to unbind
        :param add: Whether to add to functions list or replace all
        """
        self.createBind(key="<Button-1>", func=func, add=add)

    def click(self, animate=True):
        """Manually call the function that is called when this element is left clicked."""
        value = self._callBind("<Button-1>")
        if animate:
            self.app.widget.update()
            sleep(0.15)
            self._callBind("<ButtonRelease-1>")
        return value

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






























