"""OptionMenu class that inherits Element"""

import tkinter as tk

from generallibrary import SigInfo
from generallibrary.types import strToDynamicType

from generalgui.element import Element


class OptionMenu(Element):
    """
    Controls one tkinter OptionMenu
    """
    def __init__(self, parentPage, options, default=None, func=None, **parameters):
        """
        Create a OptionMenu element that controls an OptionMenu.

        :param generalgui.Page parentPage: Parent page
        :param list[str or float] options: List of options
        :param str or float or None default: What should be shown before selection, doesn't need to be an option.
        :param function func: A function that is triggered when an option is pressed. 'Value' argument is passed if needed.
        :param parameters: Both config and pack parameters together
        """
        if func and len(SigInfo(func).leadingArgNames) < 1:
            oldFunc = func
            func = lambda _: oldFunc()
        self._options = options
        self._tkString = tk.StringVar()
        self._default = default
        super().__init__(parentPage, tk.OptionMenu, variable=self._tkString, value=options[0], command=func, values=options[1:], **parameters)

        self._updateDefault()

    def _updateDefault(self):
        """
        Update the string being shown after options has been changed.
        """
        if self.getValue() not in self._options:
            if self._default is None:
                if self._options:
                    self._tkString.set(self._options[0])
                else:
                    self._tkString.set("EMPTY")
            else:
                self._tkString.set(self._default)

        isEmpty = not self._options
        self.widget.config(fg="gray" if isEmpty else "black")
        self.widget.config(activeforeground="gray" if isEmpty else "black")
        self.widget.config(cursor="arrow" if isEmpty else "hand2")

    def removeOptions(self):
        """
        Removes all options.
        """
        self.widget["menu"].delete(0, "end")
        self._options = []
        self._updateDefault()

    def addOption(self, *options):
        """
        Adds an option

        :param float or str options: Options to be added
        """
        for option in options:
            self.widget["menu"].add_command(label=option, command=tk._setit(self._tkString, option))
        self._options.extend(options)
        self._updateDefault()

    def getOptions(self):
        """
        Get a list of the supplied options.
        """
        return self._options

    def setValue(self, option):
        """
        Set the selected option.

        :param any option: Can be an option, random string or None to reset to default
        """
        self._tkString.set(option)
        self._updateDefault()

    def getDefault(self):
        """
        Get the supplied default value, if default is None then it doesn't return index 0, but None.
        """
        return self._default

    def setDefault(self, default):
        """
        Change the default value. If current value is old default then it will be changed as well.

        :param str or None default: New default value
        """
        self._default = default
        self._updateDefault()

    def getValue(self):
        """
        Get the currently shown value.
        """
        value = self._tkString.get()
        if (dynValue := strToDynamicType(value)) in self._options:
            return dynValue
        else:
            return value





