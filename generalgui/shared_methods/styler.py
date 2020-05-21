
from generallibrary.iterables import SortedList

from generalgui.shared_methods.decorators import style


class StyleHandler(list):
    """
    Handles styles for an element, could be it's own package.
    """
    def __init__(self, changeFunc, getOriginalFunc):
        """
        :param function[dict] -> None changeFunc: Function that is called when a style is enabled or disabled.
            Produces a kwargs dict that have all styles merged together.
            Can for example be "lambda kwargs: self.widgetConfig(**kwargs)".
        :param function[str] -> Any getOriginalFunc: Function that fethes the original value somehow.
            Only called the first time StyleHandles sees a new key.
            The resulting value is put inside the originalStyle which always is active with priority 0.
            Can for example be "lambda key: self.getWidgetConfig(key)".
        """
        self.changeFunc = changeFunc
        self.getOriginalFunc = getOriginalFunc
        self.styles = SortedList(getValueFunc=lambda obj: obj.priority)
        self.highestPriority = 0
        self.allStyles = {}

        self.originalStyle = self.createStyle("Original", priority=0)
        self.originalStyle.enable()

    def createStyle(self, name, priority=None, **kwargs):
        """
        Create a new style and automatically add it to this StyleHandler.

        :param str name: Name of new style
        :param float priority: Priority value, originalStyle has priority 0. If left as None then it becomes highestPriority + 1.
        :param kwargs: Keys and values for new style.
        """
        if priority is None:
            priority = self.highestPriority + 1
        self.highestPriority = max(priority, self.highestPriority)

        if name in self.allStyles:
            self.delete(name)

        style = Style(self, name, priority, **kwargs)
        self.allStyles[name] = style
        return style

    def update(self):
        """
        Iterates all active styles to merge them and then uses changeFunc to send new kwargs.
        """
        kwargs = {}
        # Iterate normally, higher priority styles will overwrite lower ones
        for style in self.styles:
            for key, value in style.kwargs.items():
                kwargs[key] = value
        self.changeFunc(kwargs)

    @style
    def delete(self, style):
        """
        Delete a style by name or style by disabling first and then deleting from allStyles.

        :param str or Style style: Style to be deleted
        """
        style.disable()
        del self.allStyles[style.name]

    @style
    def enable(self, style):
        """
        Enables a style by name or style.

        :param str or Style style: Style to be enabled.
        """
        for key, value in style.kwargs.items():
            if key not in self.originalStyle.kwargs:
                originalValue = self.getOriginalFunc(key)
                self.originalStyle.kwargs[key] = originalValue

        self.styles.add(style)
        self.update()

    @style
    def disable(self, style):
        """
        Disables a style by name or style.

        :param str or Style style: Style to be enabled.
        """
        if style in self.styles:
            self.styles.remove(style)
        self.update()

class Style:
    """
    A specific style.
    """
    def __init__(self, styler, name, priority, **kwargs):
        self.styler = styler
        self.name = name
        self.priority = priority
        self.kwargs = kwargs

    def enable(self):
        """
        Enables a style by name or style.
        """
        self.styler.enable(self)

    def disable(self):
        """
        Disables a style by name or style.
        """
        self.styler.disable(self)
