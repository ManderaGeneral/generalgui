"""Element list class that inherits Page"""

from generalgui import Grid

from generalvector import Vec2

class ElementList(Grid):
    """
    Controls any amount of elements and stacks them nicely.
    Elements are added to grid automatically.
    """
    def __init__(self, parentPage=None, startPos=Vec2(0), firstStep=Vec2(0, 1), secondStep=Vec2(1, 0), maxFirstSteps=5, **parameters):
        """

        :param generalgui.Page parentPage:
        :param Vec2 startPos:
        :param Vec2 firstStep:
        :param Vec2 secondStep:
        :param int maxFirstSteps:
        :param parameters:
        """
        super().__init__(parentPage=parentPage, **parameters)

        self.startPos = startPos
        self.firstStep = firstStep
        self.secondStep = secondStep
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
            element.grid(self.getFirstPatternPos(startPos=self.startPos, firstStep=self.firstStep, secondStep=self.secondStep, maxFirstSteps=self.maxFirstSteps))



