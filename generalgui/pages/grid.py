"""Grid class that inherits Page"""

from generalgui import Label, Page

from generalvector import Vec2


class Grid(Page):
    """
    Controls a grid, inherits Page.
    """
    def __init__(self, parentPage=None, **parameters):
        super().__init__(parentPage=parentPage, **parameters)

    def getGridElement(self, pos):
        """
        Returns the element in a certain position in grid, or None

        :param Vec2 pos: Grid position to check
        """
        if slave := self.getBaseWidget().grid_slaves(column=pos.x, row=pos.y):
            return slave[0].element

    def getGridPos(self, element):
        """
        Returns position of an element that's in this grid as a Vec2.

        :param element:
        :raises AttributeError: If element not in self
        """
        if element.parentPage != self:
            raise AttributeError(f"{element}'s parent is {element.parentPage}, not {self}")

        gridInfo = element.widget.grid_info()

        if "column" not in gridInfo or "row" not in gridInfo:
            raise AttributeError(f"{gridInfo} missing column and or row")

        return Vec2(gridInfo["column"], gridInfo["row"])

    def getGridSize(self):
        """
        Get current grid size as a Vec2.
        """
        size = self.getBaseWidget().grid_size()
        return Vec2(size[0], size[1])

    def fillGrid(self, eleCls, start, size, values=None, removeExcess=False, **parameters):
        """
        Fill grid with values, using a start position and a size.

        :param class eleCls: Class to be created in each cell
        :param Vec2 start: Start position
        :param Vec2 size: Size of values as Vec2, needs to match values len
        :param values: Values to be given to object as 'value' parameter
        :param removeExcess: Whether to remove cells with a greater position than fill area
        :param parameters: Parameters to be given to objects
        """
        if values is not None:
            values = list(values)

        currentSize = self.getGridSize()

        maxSize = currentSize.max(start + size)
        fillRange = start.range(size)


        for pos in Vec2(0).range(maxSize):
            if fillRange and pos == fillRange[0]:
                if (element := self.getGridElement(pos)) and element.__class__ == eleCls:
                    if eleCls == Label and values:
                        element.setValue(values[0])
                else:
                    if element:
                        element.remove()
                    value = values[0] if values else None
                    eleCls(self, column=pos.x, row=pos.y, value=value, **parameters)

                    # element.createStyle("Hover", "<Enter>", "<Leave>", bg="white")

                del fillRange[0]
                if values:
                    del values[0]
            elif removeExcess and not pos <= start + size - 1:
                if element := self.getGridElement(pos):
                    element.remove()

    def getFirstElementPos(self, startPos, step):
        pos = startPos
        while True:
            if element := self.getGridElement(pos):
                return element
            pos += step
            if not pos.inrange(Vec2(0, 0), self.getGridSize()):
                return None

    def addToColumn(self, element, column):
        pos = Vec2(column, self.getGridSize().y)
        element.grid(self.getFirstElementPos(pos, Vec2(0, -1)) + Vec2(0, 1))

    def addInPattern(self, element, start=Vec2(0), firstStep=Vec2(0, 1), secondStep=Vec2(1, 0), maxFirstSteps=5):
        pos = start
        while True:
            for i in range(maxFirstSteps):
                if not self.getGridElement(pos):
                    element.grid(pos)
                    return pos
                pos += firstStep
            pos = pos - firstStep * maxFirstSteps + secondStep






























