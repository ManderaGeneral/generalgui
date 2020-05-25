
from generalvector import Vec2

from generallibrary.time import Timer


class Resizer:
    """
    Scroller feature for App.
    Enables scrolling right click drag and mouse wheel.
    """
    def __init__(self):
        """
        :param generalgui.app.App self:
        """
        self.resizeables = []
        self.resizeElement = None
        self.resizeHoverElement = None
        self.resizeMouseStart = None
        self.resizeElementSize = None
        self.checkCD = Timer()
        self.resizeCD = Timer()

        self.createBind("<Button-1>", lambda event: self.startResize(event))
        self.createBind("<ButtonRelease-1>", lambda event: self.stopResize(event))
        self.motionBind = self.createBind("<Motion>", lambda event: self.checkIfResize(event), add=False)

        self.resizeStyle = self.createStyle("Resize", cursor="sizing")

    def getMouse(self, event):
        return Vec2(event.x_root, event.y_root)

    def makeResizeable(self, element):
        """
        :param generalgui.element.Element element:
        :param generalgui.app.App self:
        """
        if element not in self.resizeables:
            self.resizeables.append(element)

    def checkIfResize(self, event):
        """
        :param event:
        :param generalgui.app.App self:
        """

        mouse = self.getMouse(event)
        if self.resizeElement:
            if self.resizeCD.seconds() < 0.05:
                return
            self.resizeCD = Timer()

            newSize = (self.resizeElementSize + mouse - self.resizeMouseStart).max(Vec2(10))
            self.resizeElement.widgetConfig(width=newSize.x, height=newSize.y)

        else:
            if self.checkCD.seconds() < 0.05:
                return
            self.checkCD = Timer()

            hoveringEle = None
            for element in self.resizeables:
                elePos = Vec2(element.widget.winfo_rootx(), element.widget.winfo_rooty())
                self.resizeElementSize = Vec2(element.widget.winfo_width(), element.widget.winfo_height())
                eleLowerRight = elePos + self.resizeElementSize

                if eleLowerRight - Vec2(20) < mouse < eleLowerRight + Vec2(10):
                    hoveringEle = element
                    break

            if hoveringEle != self.resizeHoverElement:
                self.resizeHoverElement = hoveringEle
                if hoveringEle:
                    self.resizeStyle.enable()
                else:
                    self.resizeStyle.disable()

    def startResize(self, event):
        """
        :param event:
        :param generalgui.app.App self:
        """
        self.checkIfResize(event)  # If moved to fast for cooldown
        if self.resizeHoverElement:
            self.resizeElement = self.resizeHoverElement
            self.resizeMouseStart = self.getMouse(event)


    def stopResize(self, event):
        """
        :param event:
        :param generalgui.app.App self:
        """
        self.checkIfResize(event)  # To update cursor if not moving
        self.resizeElement = None
        self.checkIfResize(event)  # To update cursor if not moving





