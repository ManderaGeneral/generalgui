"""Tests for LabelEntry"""

from test.shared_methods import GuiTests

from generalgui import App, Page, LabelEntry


class LabelEntryTest(GuiTests):
    def test(self):
        labelEntry = LabelEntry(Page(App()), "hello", "defaultz")
        self.assertEqual("hello", labelEntry.label.getValue())
        self.assertEqual("defaultz", labelEntry.entry.getValue())

        labelEntry.app.remove()


