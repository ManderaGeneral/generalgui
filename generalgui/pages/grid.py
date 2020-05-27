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

    def fillGrid(self, eleCls, start, size, values=None, removeExcess=False, **parameters):
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
                    eleCls(self, column=pos.x, row=pos.y, value=value, sticky="NSEW", **parameters)

                    # element.createStyle("Hover", "<Enter>", "<Leave>", bg="white")

                del fillRange[0]
                if values:
                    del values[0]
            elif removeExcess and not pos <= start + size - 1:
                if element := self.getGridElement(pos):
                    element.remove()



