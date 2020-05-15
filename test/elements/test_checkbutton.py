"""Tests for Checkbutton"""
import unittest

from generalgui import Page, Checkbutton


class CheckbuttonTest(unittest.TestCase):
    def test_value(self):
        checkbutton = Checkbutton(Page())
        self.assertIs(False, checkbutton.getValue())

        checkbutton.setValue(True)
        self.assertIs(True, checkbutton.getValue())

        checkbutton.setValue(True)
        self.assertIs(True, checkbutton.getValue())

        checkbutton.setValue(False)
        self.assertIs(False, checkbutton.getValue())

        checkbutton.app.remove()

    def test_toggle(self):
        checkbutton = Checkbutton(Page())
        self.assertIs(False, checkbutton.getValue())

        checkbutton.toggle()
        self.assertIs(True, checkbutton.getValue())

        checkbutton.toggle()
        self.assertIs(False, checkbutton.getValue())

        checkbutton.toggle()
        self.assertIs(True, checkbutton.getValue())

        checkbutton.app.remove()

