"""Label class that inherits Element"""

import tkinter as tk

from generalgui.element import Element


class Label(Element):
    """Controls one tkinter Label"""
    def __init__(self, parentPage, value=None, hideMultiline=None, **parameters):
        """
        Create a Label element that controls a label.

        :param generalgui.Page parentPage: Parent page
        :param str value: Text to be displayed
        :param bool hideMultiline: Whether to have option to hide multilines or not
        :param parameters: Both config and pack parameters together
        """
        if value is None:
            value = ""
        if hideMultiline is None:
            hideMultiline = parentPage.hideMultiline

        self.hideMultiline = hideMultiline
        self.hiddenMultiline = hideMultiline
        self._value = value
        
        super().__init__(parentPage, tk.Label, text=self._getNewDisplayedValue(value), **parameters)

        # Multiline hiding part is a mess, but it works
        if hideMultiline:
            self.createBind("<Button-1>", self.toggleMultilines, name="HideOrShow")
            self.multilineStyle = self.createStyle("Multiline", priority=0.5, fg="gray60")
            self._updateStyle()

    def _updateStyle(self):
        if self.hideMultiline:
            if self.hiddenMultiline:
                self.multilineStyle.enable()
            else:
                self.multilineStyle.disable()

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

    def toggleMultilines(self, show=None):
        """
        Bound to <Button-1> if hideMultiline is enabled.
        Toggles self.hiddenMultiline and then updates shown text.

        :param bool show: Whether to show multiline or not. Leave as None to toggle state.
        """
        if self.hideMultiline:
            if show is None:
                show = self.hiddenMultiline
            hide = not show
            value = self.getValue()
            equals = self.hiddenMultiline == hide
            hasNewline = str(value).find("\n") != -1
            if not equals and hasNewline:
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
