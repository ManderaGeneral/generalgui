"""
Styler for app and elements.
"""

from generallibrary.iterables import SortedList
from generallibrary.types import typeChecker
from generallibrary.functions import getSignatureNames


class Styler:
    """
    Styler feature for App and Element.
    """
    def __init__(self):
        self.styleHandler = None

    def createStyle(self, name, hookBindKey=None, unhookBindKey=None, style=None, priority=None, **kwargs):
        """
        Create a new style and automatically add it to this StyleHandler.
        If hooks aren't used then you need to call enable and disable on the style object that's returned.

        :param generalgui.Element or generalgui.App self:
        :param str name: Name of new style
        :param str hookBindKey: Bind this element with this key to enable this style.
        :param str unhookBindKey: Bind this element with this key to disable this style.
        :param str or style style: Optional Style to inherit kwargs from.
        :param float priority: Priority value, originalStyle has priority 0. If left as None then it becomes highestPriority + 1.
        :param kwargs: Keys and values for new style. [prefix][styleName] to copy another style's value at the time of update.
        """
        if self.styleHandler is None:
            self.styleHandler = StyleHandler(lambda kwargs: self.widgetConfig(**kwargs), lambda key: self.getWidgetConfig(key))

        newStyle = self.styleHandler.createStyle(name=name, style=style, priority=priority, **kwargs)

        if hookBindKey:
            self.createBind(key=hookBindKey, func=newStyle.enable)
        if unhookBindKey:
            self.createBind(key=unhookBindKey, func=newStyle.disable)

        return newStyle

def styleDecorator_helper(styleHandler, style):
    """Helper for decorator."""
    if isinstance(style, str):
        if style in styleHandler.allStyles:
            style = styleHandler.allStyles[style]
        else:
            return None
            # raise AttributeError(f"Style with name {style} doesn't exist")
    if isinstance(style, Style):
        if style.name not in styleHandler.allStyles:
            raise AttributeError(f"Style with name {style.name} has been deleted")

    typeChecker(style, ("Style", None))
    return style

def styleDecorator(func):
    """
    If style isn't found then functions is silently not called!

    Decorator function to replace style name with style, can only be used in StyleHandler class.

    :param function func:
    """
    def f(styleHandler, *args, **kwargs):
        """Wrapper func."""
        if style := kwargs.get("style"):
            kwargs["style"] = styleDecorator_helper(styleHandler, style)

            if kwargs["style"] is None:
                return None

        elif "style" in (signatureNames := getSignatureNames(func)):
            index = signatureNames.index("style") - 1
            if len(args) > index:
                args = list(args)
                args[index] = styleDecorator_helper(styleHandler, args[index])

                if args[index] is None:
                    return None

        return func(styleHandler, *args, **kwargs)
    return f

class StyleHandler:
    """
    Handles styles for an element.
    """
    prefix = "$"
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
        :param kwargs: Keys and values for new style. [prefix][styleName] to copy another style's value at the time of update.
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
                if value.startswith(self.prefix):
                    if (copyStyle := self.getStyle(value[1:], onlyEnabled=True)) is None:
                        value = self.originalStyle[key]
                    else:
                        value = copyStyle[key]
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
                self.originalStyle[key] = originalValue

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

    def getStyle(self, style, onlyEnabled=False):
        """
        Get style if it exists otherwise None.

        :param str style: Name of style
        :param onlyEnabled: Whether only to enable style if it's enabled also.
        :rtype: Style
        """
        style = self.allStyles.get(style)
        if onlyEnabled and style is not None and not style.isEnabled():
            return None
        return style

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
        :param dict kwargs: Keys and values that this style want when enabled. [prefix][styleName] to copy another style's value at the time of update.
        """
        if style is not None:
            copiedKwargs = style.kwargs.copy()
            copiedKwargs.update(kwargs)
            kwargs = copiedKwargs

        # for key, value

        self.styleHandler = styleHandler
        self.name = name
        self.style = style
        self.priority = priority
        self.kwargs = kwargs

    def __getitem__(self, item):
        return self.kwargs[item]

    def __setitem__(self, key, value):
        self.kwargs[key] = value

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

    def isEnabled(self):
        """
        Get whether style is enabled or not in StyleHandler.
        """
        return self in self.styleHandler.styles

    def delete(self):
        """
        Delete style
        """
        self.styleHandler.delete(self)
