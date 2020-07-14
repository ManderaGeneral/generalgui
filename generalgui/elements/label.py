"""Label class that inherits Element"""

import tkinter as tk

from generalgui.element import Element

from generallibrary.types import strToDynamicType


class Label(Element):
    """Controls one tkinter Label"""
    def __init__(self, parentPage, value=None, hideMultiline=False, **parameters):
        """
        Create a Label element that controls a label.

        :param generalgui.Page parentPage: Parent page
        :param str value: Text to be displayed
        :param parameters: Both config and pack parameters together
        """
        if value is None:
            value = ""

        self.hiddenMultiline = hideMultiline
        self._value = value
        
        super().__init__(parentPage, tk.Label, text=self._getNewDisplayedValue(value), **parameters)

        if hideMultiline:
            self.createBind("<Button-1>", self.toggleHideMultiline, name="HideOrShow")

    def _getNewDisplayedValue(self, value):
        if self.hiddenMultiline:
            splitValue = str(value).split("\n")
            self.hiddenMultiline = len(splitValue) > 1

            if self.hiddenMultiline:
                return f"{splitValue[0]} ..."
            else:
                return splitValue[0]
        else:
            return value


    def toggleHideMultiline(self):
        """
        Bound to <Button-1> if hideMultiline is enabled.
        Toggles self.hiddenMultiline and then updates shown text.
        """
        self.hiddenMultiline = not self.hiddenMultiline
        self.setValue(self.getValue())

    def setValue(self, value):
        """
        Set value of label

        :param any value: Any value, is cast to str
        """
        if value is None:
            value = ""
        self._value = value

        self.widget["text"] = self._getNewDisplayedValue(value)

    def getValue(self):
        """
        Get value of label as a dynamic type, "tRue" becomes True for example
        """
        return self._value
        # return strToDynamicType(self.widget["text"])
