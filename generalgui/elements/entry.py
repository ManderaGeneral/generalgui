"""Entry class that inherits Element"""

import tkinter as tk

from generallibrary.types import typeChecker, strToDynamicType

from generalgui.element import Element


class Entry(Element):
    """
    Controls one tkinter Entry
    """
    def __init__(self, page, default=None, width=15, **packParameters):
        """
        Create an Entry element that controls an entry.
        """

        self._default = default

        widget = tk.Entry(page.getBaseWidget(), width=width)

        super().__init__(page, widget, **packParameters)

        if default:
            self.setValue(default)

        self.onClick(self.clearIfDefault)
        self._bind("<Control-BackSpace>", self._removeWord)
        self._bind("<Control-Delete>", lambda: self._removeWord(delete=True))
        self._bind("<FocusOut>", lambda: self.setValue(self.getDefault()) if self.getValue() == "" else None)
        self._bind("<Return>", self._clickNextButton)

    def _clickNextButton(self):
        """
        Click the first sibling that's a button when Enter key is pressed.
        :return: Click's return value or False if no button was found
        """
        for parentPage in self.getParentPages():
            for sibling in parentPage.getChildren(ignore=self):
                if typeChecker(sibling, "Button", error=False):
                    # See if click is bound
                    try:
                        return sibling.click()
                    except UserWarning:
                        pass
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

