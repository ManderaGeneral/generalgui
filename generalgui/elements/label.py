"""Label class that inherits Element"""

import tkinter as tk

from generalgui.element import Element
from generallibrary.functions import defaults

import re

class Label(Element):
    """Controls one tkinter Label"""
    def __init__(self, parentPage, value=None, hideMultiline=None, maxLen=None, **parameters):
        """
        Create a Label element that controls a label.

        :param generalgui.Page parentPage: Parent page
        :param str value: Text to be displayed
        :param bool hideMultiline: Whether to have option to hide multilines or not
        :param parameters: Both config and pack parameters together
        """
        if value is None:
            value = ""
        if maxLen:
            hideMultiline = True
        if hideMultiline is None:
            hideMultiline = parentPage.hideMultiline

        self.hideMultiline = hideMultiline
        self.hiddenMultiline = hideMultiline
        self.maxLen = maxLen
        self._value = value
        
        super().__init__(parentPage, tk.Label, text=self._getNewDisplayedValue(value), **defaults(parameters, justify="left"))

        # Multiline hiding part is a mess, but it works
        # Wont work very well if Labels's values are changed

        if hideMultiline or maxLen:
            # print(self)
            self.createBind("<Button-1>", self.toggleMultilines, name="HideOrShow")
            self.multilineStyle = self.createStyle("Multiline", priority=0.5, fg="gray60")
            self._updateStyle()

    def _updateStyle(self):
        if self.hideMultiline:
            if self.hiddenMultiline:
                self.multilineStyle.enable()
            else:
                self.multilineStyle.disable()

    def _strShouldBeHidden(self, value):
        value = str(value)
        splitValue = value.split("\n")
        multipleLines = len(splitValue) > 1
        tooLong = self.maxLen and len(value) > self.maxLen
        return multipleLines or tooLong

    def _getNewDisplayedValue(self, value):
        value = str(value)

        # This part seems weird but it works
        if self.hiddenMultiline:
            self.hiddenMultiline = self._strShouldBeHidden(value)
            if self.hiddenMultiline:
                for line in value.split("\n"):
                    if line != "":
                        break
                else:
                    line = ""

                # Remove spaces from start
                line = re.sub('^ +', '', line)

                # Limit length
                if self.maxLen and len(line) > self.maxLen:
                    line = line[0:self.maxLen]

                return f"{line} ..."

        return value

    def toggleMultilines(self, show=None):
        """
        Bound to <Button-1> if hideMultiline is enabled.
        Toggles self.hiddenMultiline and then updates shown text.

        :param bool show: Whether to show multiline or not. Leave as None to toggle state.
        """
        if self.hideMultiline and len(self.events["<Button-1>"]) == 2:  # Nothing more than style bind and multiline bind - Sketchily done though
            if show is None:
                show = self.hiddenMultiline
            hide = not show
            equals = self.hiddenMultiline == hide
            value = self.getValue()

            if not equals and self._strShouldBeHidden(value):
                # print("here", self.hideMultiline)
                self.hiddenMultiline = hide
                self.setValue(value)

    def setValue(self, value):
        """
        Set value of label

        :param any value: Any value, is cast to str
        """
        if value is None:
            value = ""
        self._value = value

        self.widget["text"] = self._getNewDisplayedValue(value)
        self._updateStyle()

    def getValue(self):
        """
        Get value of label as a dynamic type, "tRue" becomes True for example
        """
        return self._value
        # return strToDynamicType(self.widget["text"])
