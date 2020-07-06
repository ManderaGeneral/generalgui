
from generalvector import Vec2

from generallibrary.types import typeChecker


class Scroller:
    """
    Scroller feature for App.
    Enables scrolling right click drag and mouse wheel.
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

    def getVisibleFraction(self, element):
        """
        HERE ** Move to elements. Handle what happens if not shown or doesnt exist.

        :param generalgui.app.App self:
        :param generalgui.element.Element element:
        """
        canvasSize = Vec2(element.widget.winfo_width(), element.widget.winfo_height())
        scrollRegions = element.getWidgetConfig("scrollregion").split(" ")
        print(scrollRegions)
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

    def scrollButtonRelease(self, event=None):
        """

        :param generalgui.app.App self:
        :param event:
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
                # self.scrollButtonRelease(None)  # This doesn't work because B3-Motion stops being called when removed. Would have to use Motion.
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




