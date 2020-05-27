"""Grid class that inherits Page"""

from generalgui import Label, Page

from generalvector import Vec2

class Grid(Page):
    """
    Controls one Label and one Entry, very minimal page.
    """
    def __init__(self, parentPage=None, **parameters):
        super().__init__(parentPage=parentPage, **parameters)

    def getGridElement(self, pos):
        if slave := self.getBaseWidget().grid_slaves(column=pos.x, row=pos.y):
            return slave[0].element

    def getGridSize(self):
        size = self.getBaseWidget().grid_size()
        return Vec2(size[0], size[1])

    def gridLabels(self, start, end, values):
        """
        Fill grid in this frame with values.
        If labels are already in place then we just change the value.
        Any excess labels are hidden or removed.

        :param Vec2 start:
        :param Vec2 end:
        :param list[str or float] values:
        """
        currentEnd = self.getGridSize() - 1
        fillRange = start.range(end)
        maxEnd = currentEnd.max(end)

        for pos in Vec2(0, 1).range(maxEnd):
            if fillRange and pos == fillRange[0]:
                if label := self.getGridElement(pos):
                    label.setValue(values[0])
                else:
                    self.setGridElement(Label, column=pos.x, row=pos.y, value=values[0])
                del values[0]
                del fillRange[0]
            else:
                if element := self.getGridElement(pos):
                    element.remove()

    def setGridElement(self, elementClass, column, row, **parameters):
        element = elementClass(self, column=column, row=row, padx=5, sticky="NSEW", relief="groove", bg="gray85", **parameters)
        element.createStyle("Hover", "<Enter>", "<Leave>", bg="white")
        # label.createBind("<Button-1>", lambda event: print(event))
        return element

