"""Tests for LabelEntry"""

import unittest

from generalgui import Page, LabelCheckbutton


class LabelEntryTest(unittest.TestCase):
    def test(self):
        labelEntry = LabelCheckbutton(Page(), "hello")
        self.assertEqual("hello", labelEntry.label.getValue())
        self.assertIs(False, labelEntry.checkbutton.getValue())
        labelEntry.app.remove()

        labelEntry = LabelCheckbutton(Page(), "hello", True)
        self.assertEqual("hello", labelEntry.label.getValue())
        self.assertIs(True, labelEntry.checkbutton.getValue())
        labelEntry.app.remove()


