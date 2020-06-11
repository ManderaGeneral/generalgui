"""Tests for LabelEntry"""

import unittest

from generalgui import App, Page, LabelCheckbutton


class LabelEntryTest(unittest.TestCase):
    def test(self):
        labelEntry = LabelCheckbutton(Page(App()), "hello")
        self.assertEqual("hello", labelEntry.label.getValue())
        self.assertIs(False, labelEntry.checkbutton.getValue())
        labelEntry.app.remove()

        labelEntry = LabelCheckbutton(Page(App()), "hello", True)
        self.assertEqual("hello", labelEntry.label.getValue())
        self.assertIs(True, labelEntry.checkbutton.getValue())
        labelEntry.app.remove()


