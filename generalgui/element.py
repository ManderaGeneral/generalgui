"""Element for generalgui, controls a widget that's not App or Page"""

import tkinter as tk
from generallibrary.time import sleep
from generallibrary.types import typeChecker, strToDynamicType
from generallibrary.iterables import addToListInDict
from generallibrary.functions import leadingArgsCount
from generalgui.shared_methods.element_page import Element_Page
from generalgui.shared_methods.element_page_app import Element_Page_App

class Element(Element_Page, Element_Page_App):
    """
    Element is inherited by all tkinter widgets exluding App and Page.
    Shown by default. So when it's page is shown then all of page's children are shown automatically.
    """
    def __init__(self, parentPage, widget, **packParameters):
        typeChecker(parentPage, Page)

        self.setPackParameters(widget, **packParameters)

        super().__init__(parentPage, widget)

        self.pack()
        self.events = {}

    def _bind(self, key, func, add=False):
        """
        Binds a key to a function using tkinter's bind function.
        Not used directly.

        :param str key: A key from https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        :param function or None func: A function to be called or None to unbind
        :param bool add: Add to existing binds instead of overwriting
        :return:
        """
        if func is None:
            self.widget.unbind("<Button-1>")
            if key in self.events:
                del self.events[key]
        else:
            if leadingArgsCount(func) < 1:
                oldFunc = func
                func = lambda _: oldFunc()

            if add:
                addToListInDict(self.events, key, func)
            else:
                self.events[key] = [func]
            self.widget.bind(key, func, add=add)

    def _callBind(self, key):
        """
        Calls a binded key's function(s) manually.
        Not used directly.

        :param str key: A key from https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        :return: Function's return value or functions' return values in tuple in the order they were binded.
        """
        if key not in self.events:
            return None

        # Event is None when calling manually
        results = tuple(func(None) for func in self.events[key])
        if len(results) == 1:
            return results[0]
        else:
            return results

    def onClick(self, func, add=False):
        """
        Call a function when this element is left clicked.

        :param function or None func: Any function or None to unbind
        :param add: Whether to add to functions list or replace all
        """
        self._bind("<Button-1>", func, add)
    def click(self):
        """Manually call the function that is called when this element is left clicked."""
        return self._callBind("<Button-1>")

    def onRightClick(self, func, add=False):
        """
        Call a function when this element is right clicked.

        :param function or None func: Any function or None to unbind
        :param add: Whether to add to functions list or replace all
        """
        self._bind("<Button-3>", func, add)
    def rightClick(self):
        """Manually call the function that is called when this element is right clicked."""
        return self._callBind("<Button-3>")

class Text(Element):
    """Controls one tkinter Label"""
    def __init__(self, page, text):
        """
        Create a Text element that controls a label.

        :param Page page: Parent page
        :param str text: Text to be displayed
        """
        self.text = text
        widget = tk.Label(page.getBaseWidget(), text=text)

        super().__init__(page, widget)

class Button(Element):
    """
    Controls one tkinter Button
    """
    def __init__(self, page, text, func=None):
        """
        Create a Button element that controls a button.

        :param Page page: Parent page
        :param str text: Text to be displayed
        :param function func: Shortcut for Button.onClick(func)
        """
        self.text = text
        widget = tk.Button(page.getBaseWidget(), text=text)
        widget.config(cursor='hand2')

        super().__init__(page, widget)

        self._bind("<Enter>", lambda w=widget: w.config(background="gray90"))
        self._bind("<Leave>", lambda w=widget: w.config(background="SystemButtonFace"))
        self.onClick(func)

    def click(self, animate=True):
        """
        Simple animation if button's click bind is called.
        """
        if animate:
            self._callBind("<Enter>")
            self.widget.config(relief=tk.SUNKEN)
            self.app.widget.update()
            sleep(0.05)
            self.widget.config(relief=tk.RAISED)
            self._callBind("<Leave>")
        return super().click()

class Entry(Element):
    """
    Controls one tkinter Entry
    """
    def __init__(self, page, default=None):
        """
        Create an Entry element that controls an entry.
        """
        self._default = default
        widget = tk.Entry(page.getBaseWidget())

        super().__init__(page, widget)

        if default:
            self.setValue(default)
        self.onClick(self.clearIfDefault)

        self._bind("<Control-BackSpace>", self._removeWord)
        self._bind("<Control-Delete>", lambda: self._removeWord(delete=True))
        self._bind("<FocusOut>", lambda: self.setValue(self.getDefault() if self.getValue() == "" else None))
        self._bind("<Return>", self._clickNextButton)

    def _clickNextButton(self):
        """
        Click the first sibling that's a button when Enter key is pressed.
        """
        for sibling in self.getSiblings():
            if typeChecker(sibling, Button):
                sibling.click()
                break

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

    def setValue(self, value):
        """
        Set current value of entry widget, casts value to string beforehand.
        """
        if value is None:
            value = ""
        self.widget.delete(0, "end")
        self.widget.insert(tk.END, str(value))

    def clearIfDefault(self):
        """
        Clears current value if it's the current default value
        """
        if self.getValue() == strToDynamicType(self._default):
            self.setValue(None)

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




from generalgui.page import Page
































