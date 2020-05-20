

class StyleHandler:
    def __init__(self, changeFunc, getOriginalFunc):
        """

        :param function[dict] -> None changeFunc:
        :param function[str] -> Any getOriginalFunc:
        """
        self.changeFunc = changeFunc
        self.getOriginalFunc = getOriginalFunc
        self.styles = []
        self.highestPriority = 0
        self.originalStyle = self.createStyle(self, "Original")
        self.originalStyle.enable()

    def createStyle(self, name, priority=None, **kwargs):
        if priority is None:
            priority = self.highestPriority + 1
        self.highestPriority = max(priority, self.highestPriority)

        style = Style(self, name, priority, **kwargs)
        return style

    def update(self):
        pass

    # HERE **
    def enable(self, style):
        pass

    def disable(self, style):
        if style in self.styles:
            self.styles.remove(style)

class Style:
    def __init__(self, styler, name, priority, **kwargs):
        self.styler = styler
        self.name = name
        self.priority = priority
        self.kwargs = kwargs

    def enable(self):
        self.styler.enable(self)

    def disable(self):
        self.styler.disable(self)
