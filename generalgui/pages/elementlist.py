"""Element list class that inherits Page"""

from generalgui import Grid

class ElementList(Grid):
    """
    Controls any amount of elements and stacks them nicely
    """
    def __init__(self, parentPage=None, maxFirstSteps=None, **parameters):
        super().__init__(parentPage=parentPage, **parameters)
        self.maxFirstSteps = maxFirstSteps
        self.pack()

    def packPart(self, element):
        if element == self.frame:
            super().packPart(element)
        else:
            self.addInPattern(element, maxFirstSteps=self.maxFirstSteps)



