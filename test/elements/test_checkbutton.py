"""Tests for Checkbutton"""
from test.shared_methods import GuiTests

from generalgui import App, Page, Checkbutton


class CheckbuttonTest(GuiTests):
    def test_value(self):
        checkbutton = Checkbutton(Page(App()))
        self.assertIs(False, checkbutton.getValue())

        checkbutton.setValue(True)
        self.assertIs(True, checkbutton.getValue())

        checkbutton.setValue(True)
        self.assertIs(True, checkbutton.getValue())

        checkbutton.setValue(False)
        self.assertIs(False, checkbutton.getValue())

        checkbutton.app.remove()

    def test_toggle(self):
        checkbutton = Checkbutton(Page(App()))
        self.assertIs(False, checkbutton.getValue())

        checkbutton.toggle()
        self.assertIs(True, checkbutton.getValue())

        checkbutton.toggle()
        self.assertIs(False, checkbutton.getValue())

        checkbutton.toggle()
        self.assertIs(True, checkbutton.getValue())

        checkbutton.app.remove()

