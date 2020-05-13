"""Tests for Dropdown"""
from generalgui.page import Page
from generalgui.dropdown import Dropdown

import unittest

class DropdownTest(unittest.TestCase):
    def test_init(self):
        dropdown = Dropdown(Page(), [1, "hello", 3.5])
        self.assertEqual(dropdown.getOptions(), [1, "hello", 3.5])

    def test_removeOptions(self):
        dropdown = Dropdown(Page(), [1, "hello", .5])
        dropdown.removeOptions()
        self.assertEqual(dropdown.getOptions(), [])

    def test_addOption(self):
        dropdown = Dropdown(Page(), [1, "hello", 3.5])
        dropdown.addOption(4, "there")
        self.assertEqual(dropdown.getOptions(), [1, "hello", 3.5, 4, "there"])
        dropdown.addOption("Hi")
        self.assertEqual(dropdown.getOptions(), [1, "hello", 3.5, 4, "there", "Hi"])

    def test_setValue(self):
        dropdown = Dropdown(Page(), [1, "hello", 3.5])

        dropdown.setValue("hello")
        self.assertEqual(dropdown.getValue(), "hello")
        dropdown.setValue("asd")
        self.assertEqual(dropdown.getValue(), 1)
        dropdown.setValue("")
        self.assertEqual(dropdown.getValue(), 1)
        dropdown.setValue(None)
        self.assertEqual(dropdown.getValue(), 1)

    def test_getDefault(self):
        page = Page()
        self.assertEqual(None, Dropdown(page, [1, "hello", 3.5]).getDefault())
        self.assertEqual("hello", Dropdown(page, [1, "hello", 3.5], default="hello").getDefault())
        self.assertEqual("there", Dropdown(page, [1, "hello", 3.5], default="there").getDefault())
        self.assertEqual(2, Dropdown(page, [1, "hello", 3.5], default=2).getDefault())
        self.assertEqual(2.2, Dropdown(page, [1, "hello", 3.5], default=2.2).getDefault())

    def test__updateDefault(self):
        dropdown = Dropdown(Page(), [1, "hello", 3.5])

        dropdown.setValue("hello")
        dropdown._updateDefault()
        self.assertEqual("hello", dropdown.getValue())

        dropdown.setValue("doesntExist")
        dropdown._updateDefault()
        self.assertEqual(1, dropdown.getValue())

        dropdown = Dropdown(Page(), [1, "hello", 3.5], default="select")

        dropdown.setValue("hello")
        dropdown._updateDefault()
        self.assertEqual("hello", dropdown.getValue())

        dropdown.setValue("doesntExist")
        dropdown._updateDefault()
        self.assertEqual("select", dropdown.getValue())

        dropdown.setValue("1")
        dropdown._updateDefault()
        self.assertEqual(1, dropdown.getValue())

    def test_setDefault(self):
        dropdown = Dropdown(Page(), [1, "hello", 3.5])
        dropdown.setDefault("test")
        self.assertEqual(1, dropdown.getValue())
        dropdown.setValue("test")
        self.assertEqual("test", dropdown.getValue())

        dropdown.setDefault("new default")
        self.assertEqual("new default", dropdown.getValue())

        dropdown.setDefault(None)
        self.assertEqual(1, dropdown.getValue())



