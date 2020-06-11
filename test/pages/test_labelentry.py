"""Tests for LabelEntry"""

import unittest

from generalgui import App, Page, LabelEntry


class LabelEntryTest(unittest.TestCase):
    def test(self):
        labelEntry = LabelEntry(Page(App()), "hello", "defaultz")
        self.assertEqual("hello", labelEntry.label.getValue())
        self.assertEqual("defaultz", labelEntry.entry.getValue())

        labelEntry.app.remove()


