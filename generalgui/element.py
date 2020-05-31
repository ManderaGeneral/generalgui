"""Element for generalgui, controls a widget that's not App or Page"""

import inspect

from generallibrary.types import typeChecker


from generalgui.shared_methods.element_page import Element_Page
from generalgui.shared_methods.element_page_app import Element_Page_App
from generalgui.shared_methods.element_app import Element_App


class Element(Element_Page, Element_App, Element_Page_App):
    """
    Element is inherited by all tkinter widgets exluding App and Page.
    Shown by default. So when it's page is shown then all of page's children are shown automatically.
    """
    def __init__(self, parentPage, widgetClass, pack=True, makeBase=False, resizeable=False, onClick=None, **parameters):
        Element_App.__init__(self)
        Element_Page_App.__init__(self)

        typeChecker(parentPage, "Page")

        parameters["master"] = parentPage.getBaseWidget()

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


        setattr(self.widget, "element", self)
        self.parentPage = parentPage
        self.parentPart = parentPage if parentPage.baseElement is None else parentPage.baseElement
        self.app = parentPage.app

        if onClick:
            parameters["cursor"] = "hand2"
            self.createStyle("Hover", "<Enter>", "<Leave>", bg="gray90")
            self.createStyle("Click", "<Button-1>", "<ButtonRelease-1>", style="Hover", relief="sunken", fg="gray40")
            self.createBind("<Return>", self.click)
            self.onClick(onClick, add=True)

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

    def __repr__(self):
        return f"Element: {self.__class__.__name__} {self.widget}"

    def resizeable(self):
        self.app.makeResizeable(self)

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

































