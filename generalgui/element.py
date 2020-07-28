"""Element for generalgui, controls a widget that's not App or Page"""

import inspect

from generallibrary.types import typeChecker

from generalgui.shared_methods.element_page import Element_Page
from generalgui.shared_methods.element_page_app import Element_Page_App
from generalgui.shared_methods.element_app import Element_App

from generalvector import Vec2


class Element(Element_Page, Element_App, Element_Page_App):
    """
    Element is inherited by all tkinter widgets exluding App and Page.
    Shown by default. So when it's page is shown then all of page's children are shown automatically.
    """
    def __init__(self, parentPage, widgetClass, pack=True, makeBase=False, resizeable=False, onClick=None, pos=None, **parameters):
        Element_App.__init__(self)
        Element_Page_App.__init__(self)

        typeChecker(parentPage, "Page")

        if pos is not None:
            pos = Vec2(pos)
            parameters["column"] = pos.x
            parameters["row"] = pos.y

        self.app = parentPage.app
        self.parentPage = parentPage
        self.parentPart = parentPage.getBaseElement()
        parameters["master"] = self.parentPart.widget

        # Extract initialization arguments from parameters
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
        self.baseFor = None

        setattr(self.widget, "element", self)

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
        if resizeable:
            self.resizeable()
        if onClick:
            self.onClick(onClick)


    def resizeable(self):
        """Make this element resizeable"""
        self.app.makeResizeable(self)
        self.menu("Resize", Maximize=lambda x=self: x.parentPage.maximize())

    def makeBase(self):
        """
        Make this element the new base to the page it belongs to.
        If page doesn't have a top then this one becomes it as well.
        """
        self.baseFor = self.parentPage
        self.parentPage.baseElement = self
        if self.parentPage.topElement is None:
            self.parentPage.topElement = self

































