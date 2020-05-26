
from generalvector import Vec2


class Scroller:
    """
    Scroller feature for App.
    Enables scrolling right click drag and mouse wheel.
    Todo: scrollable() method just like resizable(). Probably rename those too as well
    """
    def __init__(self):
        """
        :param generalgui.app.App self:
        """
        self.scrollWheelTarget = None
        self.scrollButtonEnabled = False
        self.startCoords = None
        self.startFraction = None
        self.createBind("<MouseWheel>", self.scrollWheel)
        self.createBind("<Button-3>", self.scrollButton)
        self.createBind("<ButtonRelease-3>", self.scrollButtonRelease)
        self.createBind("<B3-Motion>", self.scrollButtonMove)

        self.scrollStyle = self.createStyle("Scroll", cursor="plus")

    def getVisibleFraction(self, element):
        """

        :param generalgui.app.App self:
        :return:
        """
        canvasSize = Vec2(element.widget.winfo_width(), element.widget.winfo_height())
        scrollRegions = element.getWidgetConfig("scrollregion").split(" ")
        scrollSize = Vec2(int(scrollRegions[2]), int(scrollRegions[3]))
        visibleFraction = canvasSize / scrollSize
        return visibleFraction

    def scrollButton(self, event):
        """

        :param generalgui.app.App self:
        :param event:
        """
        if self.scrollWheelTarget:
            if not self.scrollWheelTarget.isShown(error=False):
                self.scrollWheelTarget = None
                return

            self.startCoords = Vec2(event.x_root, event.y_root)
            self.startFraction = Vec2(self.scrollWheelTarget.widget.xview()[0], self.scrollWheelTarget.widget.yview()[0])
            self.scrollButtonEnabled = True
            self.scrollStyle.enable()

    def scrollButtonRelease(self, event):
        """

        :param generalgui.app.App self:
        :param event:
        """
        if self.scrollButtonEnabled:
            print("hi")
            self.scrollButtonEnabled = False
            self.scrollStyle.disable()


    def scrollButtonMove(self, event):
        """

        :param generalgui.app.App self:
        :param event:
        """
        if self.scrollButtonEnabled and self.scrollWheelTarget:
            if not self.scrollWheelTarget.isShown(error=False):
                self.scrollWheelTarget = None
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
            if visibleFraction.y < 1:
                self.scrollWheelTarget.widget.yview_moveto(newFraction.y)

    def scrollWheel(self, event):
        """
        When scrolling anywhere on App

        :param generalgui.app.App self:
        """
        if self.scrollWheelTarget:
            if not self.scrollWheelTarget.isShown(error=False):
                self.scrollWheelTarget = None
                return

            visibleFraction = self.getVisibleFraction(self.scrollWheelTarget)
            if visibleFraction.y >= 1:
                return

            self.scrollWheelTarget.widget.yview_scroll(round(event.delta / -1), "units")

    def setScrollTarget(self, element):
        """
        Targets an element to be scrolled if mousewheel is moved

        :param generalgui.app.App self:
        :param generalgui.element.Element element:
        """
        self.scrollWheelTarget = element

    def removeScrollTarget(self, element):
        """
        Removes mouse wheel target

        :param generalgui.app.App self:
        :param element:
        """

        if element == self.scrollWheelTarget:
            self.scrollWheelTarget = None




