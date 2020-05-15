"""Tests for LabelEntry"""

import unittest

from generalgui import Page, LabelEntry


class LabelEntryTest(unittest.TestCase):
    def test(self):
        labelEntry = LabelEntry(Page(), "hello", "defaultz")
        self.assertEqual("hello", labelEntry.label.getValue())
        self.assertEqual("defaultz", labelEntry.entry.getValue())

        labelEntry.app.remove()


