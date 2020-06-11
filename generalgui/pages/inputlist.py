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

    def packPart(self, element):
        typeChecker(element, ("Label", "Entry", "Checkbutton"))
        # self.addInPattern(element, maxFirstSteps=self.maxFirstSteps)

    def fillWithDict(self, d):
        for key, value in d.items():
            label = self.app.Label(self, key)
            pos = self.addInPattern(label, secondStep=Vec2(2, 0), maxFirstSteps=self.maxFirstSteps)

            if value is True or value is False:
                element = self.app.Checkbutton(parentPage=self, default=value)
            else:
                element = self.app.Entry(parentPage=self, default=str(value))
            element.grid(pos + Vec2(1, 0))
