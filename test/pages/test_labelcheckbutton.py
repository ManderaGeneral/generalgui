"""Tests for LabelEntry"""

from test.shared_methods import GuiTests

from generalgui import App, Page, LabelCheckbutton


class LabelCheckbuttonTest(GuiTests):
    def test_labelCheckbutton(self):
        labelCheckbutton = LabelCheckbutton(Page(App()), "hello")
        self.assertEqual("hello", labelCheckbutton.label.getValue())
        self.assertIs(False, labelCheckbutton.checkbutton.getValue())

        labelCheckbutton = LabelCheckbutton(Page(App()), "hello", True)
        self.assertEqual("hello", labelCheckbutton.label.getValue())
        self.assertIs(True, labelCheckbutton.checkbutton.getValue())


