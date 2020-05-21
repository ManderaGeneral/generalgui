"""Decorator functions"""

from generallibrary.types import typeChecker

def ignore(func):
    """
    Fix the ignore argument with a wrapper function
    """
    def f(self, ignore=None, *args, **kwargs):
        if not isinstance(ignore, (tuple, list)):
            ignore = [ignore]
        ignore = [value for value in ignore if value is not None]
        return func(self, ignore=ignore, *args, **kwargs)
    return f


def style(func):
    """
    Replace style name with style
    """
    def f(self, style, *args, **kwargs):
        if isinstance(style, str):
            if style in self.allStyles:
                style = self.allStyles[style]
            else:
                raise AttributeError(f"Style with name {style} doesn't exist")
        typeChecker(style, "Style")
        return func(self, style=style, *args, **kwargs)
    return f

