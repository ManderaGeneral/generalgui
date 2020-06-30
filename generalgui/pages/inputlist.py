"""InputList class that inherits ElementList"""

from generalgui import ElementList

from generallibrary.types import typeChecker

from generalvector import Vec2


class InputList(ElementList):
    """
    Visualizes a dictionary in a way that allows modifying values easily.
    Inherits ElementList, can not be packed to manually.
    Each key value pair has a label and a (checkbutton or entry).

    FirstStep is the default value of Vec2(0, 1).
    SecondStep is Vec2(2, 0), so almost default.
    Label is hardcoded to be Vec2(-1, 0) relative to input.
    Only option is MaxFirstSteps which defines max rows.
    """
    def __init__(self, parentPage=None, maxFirstSteps=5, **parameters):
        super().__init__(parentPage=parentPage, maxFirstSteps=maxFirstSteps, **parameters)
        self._inputElements = {}

    def setValues(self, values, add=False):
        """
        Give a dict to InputList so that it can create inputs automatically based on data inside dict.

        :param dict[str, any] values: Dictionary with unique keys containing str, bool or float
        :param add: Whether to add values or replace all
        :raises ValueError: If a value is None
        :rtype: None
        """
        if not add:
            self.removeChildren()

        for key, value in values.items():
            if value is None:
                raise ValueError(f"Value for key {key} is None - Not allowed")

            self.setInputElement(key, value)

    def getValues(self):
        """
        Returns a dictionary using the inputs as values.
        If no input is changed then the returned dictionary will be identical to the one being used to fill.
        """
        return {key: element.getValue() for key, element in self._inputElements.items()}

    def getInputElement(self, key):
        """
        Get input element, which is either an Entry or Checkbutton

        :param key:
        :rtype: generalgui.Entry or generalgui.Checkbutton
        """
        return self._inputElements.get(key, None)

    def setInputElement(self, key, value):
        """
        Set the default value of a new or existing input element, removes old if it exists.
        Automatically choses between Checkbutton and Entry

        :param str key:
        :param any value:
        """
        if key in self._inputElements:
            self.removeInput(key)

        label = self.app.Label(self, key)
        pos = self.getFirstPatternPos(secondStep=Vec2(2, 0), maxFirstSteps=self.maxFirstSteps)
        label.grid(pos)
        if value is True or value is False:
            element = self.app.Checkbutton(parentPage=self, default=value)
        else:
            element = self.app.Entry(parentPage=self, default=str(value))
        element.grid(pos + Vec2(1, 0))

        self._inputElements[key] = element

    def removeInput(self, key):
        """
        Remove label and input pair that represents a key value.

        :param str key:
        :returns: Whether input existed to be removed or not
        """
        if element := self.getInputElement(key):
            label = self.getGridElement(self.getGridPos(element) - Vec2(1, 0))
            element.remove()
            label.remove()
            del self._inputElements[key]
            return True
        return False

    def removeChildren(self, ignore=None):
        """
        Simple override to also reset inputElements.
        """
        if ignore is not None:
            raise NotImplementedError("Cannot use ignore parameter when using inputlist's removeChildren method")

        super().removeChildren(ignore=ignore)
        self._inputElements = {}

    def packPart(self, element):
        """
        Don't pack at all, only check type with whitelist

        :param element:
        """
        typeChecker(element, ("Label", "Entry", "Checkbutton"))














































