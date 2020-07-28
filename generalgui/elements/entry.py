"""Entry class that inherits Element"""

import tkinter as tk

from generallibrary.types import typeChecker, strToDynamicType

from generalgui.element import Element


class Entry(Element):
    """
    Controls one tkinter Entry
    """
    def __init__(self, parentPage, default=None, width=15, **parameters):
        """
        Create an Entry element that controls an entry.

        :param generalgui.Page parentPage: Parent page
        :param str default: What value to start with that is removed when clicking
        :param int width: Width of Entry in pixels
        :param parameters: Both config and pack parameters together
        """
        super().__init__(parentPage, tk.Entry, width=width, **parameters)

        self._default = default
        if default:
            self.setValue(default)

        self.onClick(self.clearIfDefault)
        self.createBind("<Control-BackSpace>", self._removeWord)
        self.createBind("<Control-Delete>", lambda: self._removeWord(delete=True))
        self.createBind("<FocusOut>", lambda: self.setValue(self.getDefault()) if self.getValue() == "" else None)
        self.createBind("<Return>", self._clickNextButton)

    def _clickNextButton(self):
        """
        Click the first sibling that's a button when Enter key is pressed.

        :return: Click's return value or False if no button was found
        """
        for parentPage in self.getParents():

            if self.parentPage == parentPage:
                elements = self.getSiblings()
            else:
                elements = parentPage.getChildren(ignore=self)

            for element in elements:
                if typeChecker(element, "Button", error=False):
                    return element.click()
        return False

    def _removeWord(self, delete=False):
        """
        Remove a full word or a range of repeating characters when Ctrl key is being held.

        :param delete: Whether delete key was used and we should reverse backspace method.
        """
        marker = self.widget.index(tk.INSERT)
        value = str(self.getValue())
        if delete:
            marker = len(value) - marker
            value = value[::-1]

        if marker >= 2:

            index = marker - 1
            removeChar = value[index]

            checkIndex = index - 1
            repeatingRemovedChar = True
            # Change checkIndex to be the last inclusive index of the start string
            while checkIndex >= 0:
                checkChar = value[checkIndex]
                if repeatingRemovedChar and checkChar != removeChar:
                    repeatingRemovedChar = False
                matchingAlpha = removeChar.isalpha() and checkChar.isalpha()
                matchingNumeric = removeChar.isnumeric() and checkChar.isnumeric()

                if matchingAlpha or matchingNumeric or repeatingRemovedChar:
                    checkIndex -= 1
                else:
                    break

            # Add an x to be removed from the original backspace or delete
            newValue = value[0:checkIndex + 1] + "x" + value[index + 1:]
            if delete:
                self.setValue(newValue[::-1])
                self.setMarker(len(newValue) - checkIndex - 2)
            else:
                self.setValue(newValue)
                self.setMarker(checkIndex + 2)

    def setMarker(self, index):
        """
        Move the marker inside entry widget.
        """
        self.widget.icursor(index)

    def getValue(self):
        """
        Get the current value of the entry widget, casts to dynamic type beforehand.
         | "true" -> True
         | "noNe" -> None
         | "" -> ""
         | "5.2" -> 5.2 (float)
         | "5" -> 5 (int)
        """
        return strToDynamicType(self.widget.get())

    def setValue(self, value, useDefault=True):
        """
        Set current value of entry widget, casts value to string beforehand.

        :param str or float or bool or None value: New value for entry
        :param useDefault: Whether to use default value or not if new value is None or empty
        """
        if value is None:
            value = ""
        if useDefault and value == "" and self.getDefault() is not None:
            value = self.getDefault()

        self.widget.delete(0, "end")
        self.widget.insert(tk.END, str(value))

    def clearIfDefault(self):
        """
        Clears current value if it's the current default value
        """
        if self.getValue() == strToDynamicType(self._default):
            self.setValue(None, useDefault=False)

    def getDefault(self):
        """
        Get the supplied default value
        """
        return self._default

    def setDefault(self, default):
        """
        Change the default value. If current value is old default then it will be changed as well.
        """
        if str(self.getDefault()) == str(self.getValue()):
            self.setValue(default)
        self._default = default

