
from generalvector import Vec2

from generallibrary.types import typeChecker


class Scroller:
    """
    Scroller feature for App.
    Enables scrolling right click drag and mouse wheel.
    self.scrollWheelTarget is None or a page.canvas.

    Note: I don't like how canvas is being used for target, it should all be targetting pages.
    """
    def __init__(self):
        """
        :param generalgui.app.App self:
        """
        self.scrollWheelTarget = None
        self.startCoords = None
        self.startFraction = None
        self.createBind("<MouseWheel>", self.scrollWheel)
        self.createBind("<Button-3>", self.scrollButton)
        self.createBind("<ButtonRelease-3>", self.scrollButtonRelease)
        self.createBind("<B3-Motion>", self.scrollButtonMove)

        self.scrollStyle = self.createStyle("Scroll", cursor="plus")

    def _checkEventForScrollTarget(self, event):
        if not event:
            return
        eventElement = event.widget.element
        if typeChecker(eventElement, "App", error=False):
            return

        pages = eventElement.getParentPages()
        for page in pages:
            if page.scrollable and page.mouseScroll:
                visibleFraction = self.getVisibleFraction(page.canvas)
                if not visibleFraction >= Vec2(1):
                    self.scrollWheelTarget = page.canvas
                    break

    def getVisibleFraction(self, canvas):
        """
        Get visible fraction of a canvas, not meant to be used other than by scroll feature.

        :param generalgui.app.App self:
        :param generalgui.Canvas canvas:
        :raises AttributeError: If canvas is not shown
        """
        if not canvas.isShown():
            raise AttributeError("Canvas is not shown")

        canvasSize = Vec2(canvas.widget.winfo_width(), canvas.widget.winfo_height())
        scrollRegions = canvas.getWidgetConfig("scrollregion").split(" ")
        scrollSize = Vec2(int(scrollRegions[2]), int(scrollRegions[3]))
        visibleFraction = canvasSize / scrollSize
        return visibleFraction

    def scrollButton(self, event):
        """

        :param generalgui.app.App self:
        :param event:
        """
        self._checkEventForScrollTarget(event)
        if self.scrollWheelTarget:
            self.startCoords = Vec2(event.x_root, event.y_root)
            self.startFraction = Vec2(self.scrollWheelTarget.widget.xview()[0], self.scrollWheelTarget.widget.yview()[0])
            self.scrollStyle.enable()

    def scrollButtonRelease(self):
        """

        :param generalgui.app.App self:
        """
        self.scrollWheelTarget = None
        self.scrollStyle.disable()

    def scrollButtonMove(self, event):
        """

        :param generalgui.app.App self:
        :param event:
        """
        if self.scrollWheelTarget:
            if not self.scrollWheelTarget.isShown(error=False):
                self.scrollButtonRelease()
                return

            coords = Vec2(event.x_root, event.y_root)
            mouseDiff = coords - self.startCoords
            canvasSize = Vec2(self.scrollWheelTarget.widget.winfo_width(), self.scrollWheelTarget.widget.winfo_height())
            fractionMouseDiff = mouseDiff / canvasSize

            visibleFraction = self.getVisibleFraction(self.scrollWheelTarget)
            newFraction = self.startFraction - fractionMouseDiff * visibleFraction

            if visibleFraction.x < 1:
                self.scrollWheelTarget.widget.xview_moveto(newFraction.x)
                self.openMenuOnRelease = False
            if visibleFraction.y < 1:
                self.scrollWheelTarget.widget.yview_moveto(newFraction.y)
                self.openMenuOnRelease = False

    def scrollWheel(self, event):
        """
        When scrolling anywhere on App

        :param generalgui.app.App self:
        :param event:
        """
        self._checkEventForScrollTarget(event)
        if self.scrollWheelTarget:
            if not self.scrollWheelTarget.isShown(error=False):
                self.scrollWheelTarget = None
                return

            visibleFraction = self.getVisibleFraction(self.scrollWheelTarget)
            if visibleFraction.y >= 1:
                return

            self.scrollWheelTarget.widget.yview_scroll(round(event.delta / -1), "units")




