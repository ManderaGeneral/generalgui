"""
Styler for elements.
Could be it's own package and be called Config and ConfigHandler instead.
"""

from generallibrary.iterables import SortedList
from generallibrary.types import typeChecker
from generallibrary.functions import getSignatureNames



def styleDecorator_helper(styleHandler, style):
    """Helper for decorator."""
    if isinstance(style, str):
        if style in styleHandler.allStyles:
            style = styleHandler.allStyles[style]
        else:
            raise AttributeError(f"Style with name {style} doesn't exist")
    typeChecker(style, ("Style", None))
    return style

def styleDecorator(func):
    """
    Decorator function to replace style name with style, can only be used in StyleHandler class.
    "Style" argument must not be passed through *args.

    :param function func:
    """
    def f(styleHandler, *args, **kwargs):
        """Wrapper func."""
        if style := kwargs.get("style"):
            kwargs["style"] = styleDecorator_helper(styleHandler, style)
        elif "style" in (signatureNames := getSignatureNames(func)):
            index = signatureNames.index("style") - 1
            if len(args) > index:
                args = list(args)
                args[index] = styleDecorator_helper(styleHandler, args[index])
        return func(styleHandler, *args, **kwargs)
    return f

class StyleHandler(list):
    """
    Handles styles for an element.
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

    @styleDecorator
    def createStyle(self, name, style=None, priority=None, **kwargs):
        """
        Create a new style and automatically add it to this StyleHandler.

        :param str name: Name of new style
        :param str or style style: Optional Style to inherit kwargs from.
        :param float priority: Priority value, originalStyle has priority 0. If left as None then it becomes highestPriority + 1.
        :param kwargs: Keys and values for new style.
        """
        if priority is None:
            priority = self.highestPriority + 1
        self.highestPriority = max(priority, self.highestPriority)

        if name in self.allStyles:
            self.delete(name)

        newStyle = Style(styleHandler=self, name=name, style=style, priority=priority, **kwargs)
        self.allStyles[name] = newStyle
        return newStyle

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

    @styleDecorator
    def delete(self, style):
        """
        Delete a style by name or style by disabling first and then deleting from allStyles.

        :param str or Style style: Style to be deleted
        """
        style.disable()
        del self.allStyles[style.name]

    @styleDecorator
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

    @styleDecorator
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
    A specific style. Initalized through StyleHandler.createStyle().
    """
    def __init__(self, styleHandler, name, style, priority, **kwargs):
        """
        A style that has it's own kwargs.

        :param StyleHandler styleHandler: StyleHandler that takes care of all different Styles.
        :param str name: Required name of style.
        :param str or Style style: Optional Style to inherit kwargs from.
        :param float priority: Priority value for this style, higher is stronger. Original style has 0.
        :param dict kwargs: Keys and values that this style want when enabled.
        """
        if style is not None:
            copiedKwargs = style.kwargs.copy()
            copiedKwargs.update(kwargs)
            kwargs = copiedKwargs

        self.styleHandler = styleHandler
        self.name = name
        self.style = style
        self.priority = priority
        self.kwargs = kwargs

    def enable(self):
        """
        Enables a style by name or style.
        """
        self.styleHandler.enable(self)

    def disable(self):
        """
        Disables a style by name or style.
        """
        self.styleHandler.disable(self)



