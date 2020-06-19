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
        if not pos >= Vec2(0, 0):
            return None

        pos = pos.sanitize(ints=True)

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

        gridInfo = element.getTopWidget().grid_info()

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
        currentSize = self.getGridSize()

        maxSize = currentSize.max(start + size)
        fillRange = start.range(size)

        if values is not None:
            values = list(values)
            if len(values) != len(fillRange):
                raise ValueError("Values length doesn't match fillRange's")

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

    def confinePos(self, pos, maxPos=None):
        """
        Returns a confined pos between 0 and gridSize - 1

        :param Vec2 pos:
        :param Vec2 maxPos:
        """
        if maxPos is None:
            maxPos = self.getGridSize() - 1
        return pos.confineTo(Vec2(0, 0), maxPos, margin=0.5)

    def _traverse(self, checkPosFunc, startPos, step=None, maxPos=None, confine=False, maxSteps=100):
        if step is None:
            step = Vec2(0)
        if maxPos is None:
            maxPos = self.getGridSize() - 1
        if maxPos == -1:
            return None

        pos = startPos.sanitize(ints=True)
        step.sanitize(ints=True)

        pos = self.confinePos(pos, maxPos)

        for i in range(maxSteps + 1):
            if (result := checkPosFunc(pos)) is not None:
                return result
            if step == 0:
                break
            pos += step
            if confine:
                pos = self.confinePos(pos, maxPos)
            if pos == startPos or not pos.inrange(Vec2(0, 0), maxPos):
                break
        return None

    def getFirstElementPos(self, startPos, step=None, confine=False, maxSteps=100):
        """
        Get position of first found element.
        Grid's upper left corner is always Vec2(0, 0).
        Lower right corner is grid size - 1.

        :param Vec2 startPos: Inclusive position to start search
        :param Vec2 step: Directional Vec2 to be used as step for each iteration
        :param confine: Whether to confine search or not
        :param int maxSteps: Maximum amount of steps to take without result before returning None
        """
        def checkPosFunc(pos):
            """Func passed to traverse"""
            if self.getGridElement(pos):
                return pos

        return self._traverse(checkPosFunc=checkPosFunc, startPos=startPos, step=step, confine=confine, maxSteps=maxSteps)

    def getFirstEmptyPos(self, startPos, step=None, confine=False, maxSteps=100):
        """
        Get position of first empty pos.
        Grid's upper left corner is always Vec2(0, 0).
        Lower right corner is grid size - 1.

        :param Vec2 startPos: Inclusive position to start search
        :param Vec2 step: Directional Vec2 to be used as step for each iteration
        :param confine: Whether to confine search or not
        :param int maxSteps: Maximum amount of steps to take without result before returning None
        """
        def checkPosFunc(pos):
            """Func passed to traverse"""
            if not self.getGridElement(pos):
                return pos

        gridSize = self.getGridSize()
        if gridSize == 0:
            return startPos.max(0)

        # maxPos = gridSize - 1 + step.absolute()
        maxPos = gridSize - 1

        traverse = self._traverse(checkPosFunc=checkPosFunc, startPos=startPos, step=step, maxPos=maxPos, confine=confine, maxSteps=maxSteps)
        return traverse

    def getFirstPatternPos(self, startPos=Vec2(0), firstStep=Vec2(0, 1), secondStep=Vec2(1, 0), maxFirstSteps=5):
        """
        Get position of first empty pos in pattern.
        When firstStep has been made maxFirstSteps times we subtract all firstSteps and then make one secondStep.
        If maxfirststeps is 1 then only second step is used.

        :param Vec2 startPos: Inclusive position to start search
        :param Vec2 firstStep: Directional Vec2 to be used as step for each maxFirstSteps
        :param Vec2 secondStep: Directional Vec2 to be used as step for each time firstStep has been made maxFirstSteps times
        :param maxFirstSteps: Number of firstSteps before one secondStep
        """
        pos = startPos
        while True:
            for i in range(maxFirstSteps):
                if not self.getGridElement(pos):
                    return pos
                pos += firstStep
            pos = pos - firstStep * maxFirstSteps + secondStep

    def appendToColumn(self, part, column):
        """
        Append a part to column, after the last possibly existing cell

        :param generalgui.element.Element or generalgui.page.Page part:
        :param int column: Which column to append to
        :return: Position of filled cell
        """
        firstEmptyPos = self.getFirstEmptyPos(Vec2(column, 0), Vec2(0, 1))
        if firstEmptyPos is None:
            firstEmptyPos = Vec2(column, self.getGridSize().y)
        part.grid(firstEmptyPos)
        return firstEmptyPos

    def appendToRow(self, part, row):
        """
        Append a part to column, after the last possibly existing cell

        :param generalgui.element.Element or generalgui.page.Page part:
        :param int row: Which row to append to
        :return: Position of filled cell
        """
        firstEmptyPos = self.getFirstEmptyPos(Vec2(0, row), Vec2(1, 0))
        if firstEmptyPos is None:
            firstEmptyPos = Vec2(self.getGridSize().x, row)
        part.grid(firstEmptyPos)
        return firstEmptyPos






























