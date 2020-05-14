"""Tests for Button"""
import tkinter as tk
import unittest

from generalgui import Page, Label


class LabelTest(unittest.TestCase):
    def test_label(self):
        for page in Page(), Page(width=200):
            label = Label(page, "hello")
            self.assertEqual(label.parentPage, page)
            self.assertIs(label.widget.element, label)
            self.assertFalse(label.isShown())

            label.show(mainloop=False)
            self.assertTrue(label.isShown())

            page.app.remove()
            self.assertRaises(tk.TclError, label.isShown)

    def test_value(self):
        label = Label(Page(), "hello")

        label.setValue("test")
        self.assertEqual("test", label.getValue())

        label.setValue(None)
        self.assertEqual("", label.getValue())

        label.setValue("")
        self.assertEqual("", label.getValue())

        label.setValue(True)
        self.assertEqual("True", label.getValue())

