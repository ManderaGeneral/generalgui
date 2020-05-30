"""
Resizer for app.
"""

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
        self.checkTimer = Timer()
        self.resizeTimer = Timer()
        self.resizeAfterID = None

        self.createBind("<ButtonPress-1>", lambda event: self.startResize(event))
        self.createBind("<ButtonRelease-1>", lambda event: self.app.widget.after(10, lambda: self.stopResize(event)))
        self.motionBind = self.createBind("<Motion>", lambda event: self.checkIfResize(event), add=False)

        self.resizeStyle = self.createStyle("Resize", cursor="sizing")

    def makeResizeable(self, element):
        """
        :param generalgui.element.Element element:
        :param generalgui.app.App self:
        """
        if element not in self.resizeables:
            self.resizeables.append(element)

    def _scrubEle(self, element, scrubHidden=True):
        if element is None:
            return False
        if not element.exists():
            return True
        if scrubHidden and not element.isShown():
            return True

        return False

    resizeCD = 0.1
    checkCD = 0.05
    def checkIfResize(self, event):
        """
        :param event:
        :param generalgui.app.App self:
        """
        if self.resizeHoverElement and not self.resizeHoverElement.isShown(error=False):
            self.resizeHoverElement = None
            self.resizeElement = None
            self.resizeStyle.disable()

        mouse = self.getMouse(event)

        if self.resizeAfterID:
            self.app.widget.after_cancel(self.resizeAfterID)
            self.resizeAfterID = None

        if self.resizeElement:
            if self.resizeTimer.seconds() < self.resizeCD:
                msDelay = round((self.resizeCD - self.resizeTimer.seconds()) / 1000) + 10
                self.resizeAfterID = self.app.widget.after(msDelay, self.checkIfResize, event)
                return
            self.resizeTimer = Timer()

            newSize = (self.resizeElementSize + mouse - self.resizeMouseStart).max(Vec2(10))
            self.resizeElement.widgetConfig(width=newSize.x, height=newSize.y)

        else:
            if self.checkTimer.seconds() < self.checkCD:
                return
            self.checkTimer = Timer()

            hoveringEle = None
            removedElements = []
            for element in self.resizeables:
                if not element.exists():
                    removedElements.append(element)
                    continue
                if not element.isShown():
                    continue

                elePos = Vec2(element.widget.winfo_rootx(), element.widget.winfo_rooty())
                self.resizeElementSize = Vec2(element.widget.winfo_width(), element.widget.winfo_height())
                eleLowerRight = elePos + self.resizeElementSize

                if eleLowerRight - Vec2(20) < mouse < eleLowerRight + Vec2(10):
                    hoveringEle = element
                    break

            for removedElement in removedElements:
                self.resizeables.remove(removedElement)

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
            return "break"


    def stopResize(self, event):
        """
        :param event:
        :param generalgui.app.App self:
        """
        self.checkIfResize(event)  # To update cursor if not moving
        self.resizeElement = None
        self.checkIfResize(event)  # To update cursor if not moving





