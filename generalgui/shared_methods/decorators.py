
def ignore(func):
    def f(self, ignore=None, *args, **kwargs):
        if not isinstance(ignore, (tuple, list)):
            ignore = [ignore]
        ignore = [value for value in ignore if value is not None]
        return func(self, ignore=ignore, *args, **kwargs)
    return f
