"""Tests for OptionMenu"""
import unittest

from generalgui import Page, OptionMenu


class OptionMenuTest(unittest.TestCase):
    def test_init(self):
        optionMenu = OptionMenu(Page(), [1, "hello", 3.5])
        self.assertEqual(optionMenu.getOptions(), [1, "hello", 3.5])

    def test_removeOptions(self):
        optionMenu = OptionMenu(Page(), [1, "hello", .5])
        optionMenu.removeOptions()
        self.assertEqual(optionMenu.getOptions(), [])

    def test_addOption(self):
        optionMenu = OptionMenu(Page(), [1, "hello", 3.5])
        optionMenu.addOption(4, "there")
        self.assertEqual(optionMenu.getOptions(), [1, "hello", 3.5, 4, "there"])
        optionMenu.addOption("Hi")
        self.assertEqual(optionMenu.getOptions(), [1, "hello", 3.5, 4, "there", "Hi"])

    def test_setValue(self):
        optionMenu = OptionMenu(Page(), [1, "hello", 3.5])

        optionMenu.setValue("hello")
        self.assertEqual(optionMenu.getValue(), "hello")
        optionMenu.setValue("asd")
        self.assertEqual(optionMenu.getValue(), 1)
        optionMenu.setValue("")
        self.assertEqual(optionMenu.getValue(), 1)
        optionMenu.setValue(None)
        self.assertEqual(optionMenu.getValue(), 1)

    def test_getDefault(self):
        page = Page()
        self.assertEqual(None, OptionMenu(page, [1, "hello", 3.5]).getDefault())
        self.assertEqual("hello", OptionMenu(page, [1, "hello", 3.5], default="hello").getDefault())
        self.assertEqual("there", OptionMenu(page, [1, "hello", 3.5], default="there").getDefault())
        self.assertEqual(2, OptionMenu(page, [1, "hello", 3.5], default=2).getDefault())
        self.assertEqual(2.2, OptionMenu(page, [1, "hello", 3.5], default=2.2).getDefault())

    def test__updateDefault(self):
        optionMenu = OptionMenu(Page(), [1, "hello", 3.5])

        optionMenu.setValue("hello")
        optionMenu._updateDefault()
        self.assertEqual("hello", optionMenu.getValue())

        optionMenu.setValue("doesntExist")
        optionMenu._updateDefault()
        self.assertEqual(1, optionMenu.getValue())

        optionMenu = OptionMenu(Page(), [1, "hello", 3.5], default="select")

        optionMenu.setValue("hello")
        optionMenu._updateDefault()
        self.assertEqual("hello", optionMenu.getValue())

        optionMenu.setValue("doesntExist")
        optionMenu._updateDefault()
        self.assertEqual("select", optionMenu.getValue())

        optionMenu.setValue("1")
        optionMenu._updateDefault()
        self.assertEqual(1, optionMenu.getValue())

    def test_setDefault(self):
        optionMenu = OptionMenu(Page(), [1, "hello", 3.5])
        optionMenu.setDefault("test")
        self.assertEqual(1, optionMenu.getValue())
        optionMenu.setValue("test")
        self.assertEqual("test", optionMenu.getValue())

        optionMenu.setDefault("new default")
        self.assertEqual("new default", optionMenu.getValue())

        optionMenu.setDefault(None)
        self.assertEqual(1, optionMenu.getValue())



