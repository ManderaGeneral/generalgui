"""Tests for Button"""
import tkinter as tk
from test.shared_methods import GuiTests

from generalgui import App, Page, Label


class LabelTest(GuiTests):
    def test_label(self):
        for page in Page(App()), Page(App(), width=200, height=200):
            label = Label(page, "hello")
            self.assertEqual(label.parentPage, page)
            self.assertIs(label.widget.element, label)
            self.assertFalse(label.isShown())

            label.show(mainloop=False)
            self.assertTrue(label.isShown())

            page.app.remove()
            self.assertRaises(tk.TclError, label.isShown)

    def test_value(self):
        label = Label(Page(App()), "hello")

        label.setValue("test")
        self.assertEqual("test", label.getValue())

        label.setValue(None)
        self.assertEqual("", label.getValue())

        label.setValue("")
        self.assertEqual("", label.getValue())

        label.setValue(True)
        self.assertEqual(True, label.getValue())

