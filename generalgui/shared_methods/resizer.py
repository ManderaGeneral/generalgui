
from generalvector import Vec2


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
        self.motionBind = None
        self.resizeMouseStart = None
        self.resizeSizeStart = None

        self.createBind("<Button-1>", lambda event: self.startResize(event))
        self.createBind("<ButtonRelease-1>", lambda event: self.stopResize())

        self.resizeStyle = self.createStyle("Resize", cursor="sizing")

    def resizeable(self, element):
        """
        :param generalgui.element.Element element:
        :param generalgui.app.App self:
        """
        if element not in self.resizeables:
            self.resizeables.append(element)

    def resize(self, event):
        """
        :param event:
        :param generalgui.app.App self:
        """
        print(event)
        mouse = Vec2(event.x_root, event.y_root)
        newSize = (self.resizeSizeStart + mouse - self.resizeMouseStart).max(Vec2(10))
        self.resizeElement.widgetConfig(width=newSize.x, height=newSize.y)

    def startResize(self, event):
        """
        :param event:
        :param generalgui.app.App self:
        """
        for element in self.resizeables:
            mouse = Vec2(event.x_root, event.y_root)
            elePos = Vec2(element.widget.winfo_rootx(), element.widget.winfo_rooty())
            eleSize = Vec2(element.widget.winfo_width(), element.widget.winfo_height())
            eleLowerRight = elePos + eleSize
            relativeMouse = eleLowerRight - mouse

            if relativeMouse.length() < 10:
                self.resizeElement = element
                # HERE ** Always have this motion bind active so we can change cursor before clicking
                self.motionBind = self.createBind("<Motion>", lambda event: self.resize(event), add=False)
                self.resizeMouseStart = mouse
                self.resizeSizeStart = eleSize

                self.resizeStyle.enable()

    def stopResize(self):
        """
        :param generalgui.app.App self:
        """
        if self.resizeElement:
            self.resizeStyle.disable()
            self.resizeElement = None

        if self.motionBind is not None:
            self.removeBind("<Motion>", self.motionBind)
            self.motionBind = None






