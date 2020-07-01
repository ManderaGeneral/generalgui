"""Tests for InputList"""

from test.shared_methods import GuiTests

from generalgui import App, Page, InputList


class InputListTest(GuiTests):
    def test_getAndSetValues(self):
        inputList = InputList(Page(App()))

        self.assertEqual({}, inputList.getValues())

        with self.assertRaises(ValueError):
            inputList.setValues({"test": None})

        self.assertEqual({}, inputList.getValues())

        inputList.setValues({"test": True})
        self.assertEqual({"test": True}, inputList.getValues())

        inputList.setValues({"test": True})
        self.assertEqual({"test": True}, inputList.getValues())

        inputList.setValues({"test": "entry now"}, add=True)
        self.assertEqual({"test": "entry now"}, inputList.getValues())

        inputList.setValues({"another": "foobar"}, add=True)
        self.assertEqual({"test": "entry now", "another": "foobar"}, inputList.getValues())

        inputList.setValues({"another": "foobar"})
        self.assertEqual({"another": "foobar"}, inputList.getValues())

    def test_getAndSetInputElements(self):
        inputList = InputList(Page(App()))

        inputList.setValues({"test": True, "entry": "text"})
        self.assertEqual(True, inputList.getInputElement("test").getValue())
        self.assertEqual("text", inputList.getInputElement("entry").getValue())

        inputList.setInputElement("test", 5)
        self.assertEqual(5, inputList.getInputElement("test").getValue())
        self.assertEqual("Entry", inputList.getInputElement("entry").__class__.__name__)

        inputList.setInputElement("entry", False)
        self.assertEqual(False, inputList.getInputElement("entry").getValue())
        self.assertEqual("Checkbutton", inputList.getInputElement("entry").__class__.__name__)

        inputList.setInputElement("new", "text here")
        self.assertEqual("text here", inputList.getInputElement("new").getValue())
        self.assertEqual("Entry", inputList.getInputElement("new").__class__.__name__)

    def test_removeInput(self):
        inputList = InputList(Page(App()))

        inputList.setValues({"test": True})
        self.assertEqual({"test": True}, inputList.getValues())

        self.assertTrue(inputList.removeInput("test"))
        self.assertEqual({}, inputList.getValues())

        self.assertFalse(inputList.removeInput("test"))

    def test_removeChildren(self):
        inputList = InputList(Page(App()))

        inputList.setValues({"test": True, "entry": "text"})
        self.assertEqual({"test": True, "entry": "text"}, inputList.getValues())

        inputList.removeChildren()
        self.assertEqual({}, inputList.getValues())

        with self.assertRaises(NotImplementedError):
            inputList.removeChildren(ignore=["foobar"])


















