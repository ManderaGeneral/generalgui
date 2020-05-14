"""Tests for Button"""
import tkinter as tk
import unittest

from generalgui import Page, Label


class LabelTest(unittest.TestCase):
    def test_label(self):
        for page in Page(), Page(width=200):
            text = Label(page, "hello")
            self.assertEqual(text.parentPage, page)
            self.assertIs(text.widget.element, text)
            self.assertFalse(text.isShown())

            text.show(mainloop=False)
            self.assertTrue(text.isShown())

            page.app.remove()
            self.assertRaises(tk.TclError, text.isShown)


