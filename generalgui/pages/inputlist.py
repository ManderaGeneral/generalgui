"""InputList class that inherits ElementList"""

from generalgui import ElementList

from generallibrary.types import typeChecker

from generalvector import Vec2


class InputList(ElementList):
    """
    Controls only labelcheckbuttons and labelentries, puts them in nice grid
    """
    def __init__(self, parentPage=None, maxFirstSteps=None, **parameters):
        super().__init__(parentPage=parentPage, maxFirstSteps=maxFirstSteps, **parameters)
        self.inputElements = {}

    def packPart(self, element):
        # Don't pack at all, only check type with whitelist
        typeChecker(element, ("Label", "Entry", "Checkbutton"))

    def fillWithValues(self, values, add=False):
        if not add:
            self.removeChildren()

        for key, value in values.items():
            label = self.app.Label(self, key)
            pos = self.getFirstPatternPos(secondStep=Vec2(2, 0), maxFirstSteps=self.maxFirstSteps)
            label.grid(pos)

            if value is True or value is False:
                element = self.app.Checkbutton(parentPage=self, default=value)
            else:
                element = self.app.Entry(parentPage=self, default=str(value))

            element.grid(pos + Vec2(1, 0))
            self.addInputElement(key, element)

    def getValues(self):
        return {key: element.getValue() for key, element in self.inputElements.items()}

    def addInputElement(self, key, element):
        if key in self.inputElements:
            raise KeyError(f"Key {key} already exists in inputElements")

        self.inputElements[key] = element

    def removeChildren(self, ignore=None):
        super().removeChildren(ignore=ignore)
        self.inputElements = {}
