"""Element list class that inherits Page"""

from generalgui import Grid

class ElementList(Grid):
    """
    Controls any amount of elements and stacks them nicely.
    Elements are added to grid automatically.
    """
    def __init__(self, parentPage=None, maxFirstSteps=5, **parameters):
        super().__init__(parentPage=parentPage, **parameters)
        self.maxFirstSteps = maxFirstSteps
        self.pack()

    def packPart(self, element):
        """
        Used by element.pack()
        Override this method to automatically pack children in pattern in grid, unless it's ElementList's frame.

        :param generalgui.element.Element element:
        """
        if element == self.frame:
            super().packPart(element)
        else:
            self.addInPattern(element, maxFirstSteps=self.maxFirstSteps)



