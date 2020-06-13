"""Tests for Button"""
import tkinter as tk
from test.shared_methods import GuiTests

from generalgui import App, Page, Label


class LabelTest(GuiTests):
    def test_label(self):
        app = App()
        for page in Page(app), Page(app, width=200, height=200):
            label = Label(page)
            self.assertEqual("", label.getValue())

            label = Label(page, "hello")
            self.assertEqual(label.parentPage, page)
            self.assertIs(label.widget.element, label)
            self.assertFalse(label.isShown())

            label.show(mainloop=False)
            self.assertTrue(label.isShown())

            page.remove()
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

