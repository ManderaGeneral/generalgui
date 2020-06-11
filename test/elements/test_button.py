"""Tests for Button"""
import tkinter as tk

from test.shared_methods import GuiTests

from generalgui import Page, Button, App


class ButtonTest(GuiTests):
    def test_button(self):
        for page in Page(App()), Page(App(), width=200, height=200):
            button = Button(page, "hello", lambda: 5)
            self.assertEqual(button.parentPage, page)
            self.assertIs(button.widget.element, button)
            self.assertFalse(button.isShown())

            button.show(mainloop=False)
            self.assertTrue(button.isShown())

            self.assertEqual([5], button.click())

            page.app.remove()
            self.assertRaises(tk.TclError, button.isShown)

    def test_value(self):
        button = Button(Page(App()), "start")
        self.assertEqual("start", button.getValue())

        button.setValue("changed")
        self.assertEqual("changed", button.getValue())

        button.setValue("")
        self.assertEqual("", button.getValue())

        button.setValue(True)
        self.assertIs(True, button.getValue())

        button.setValue(None)
        self.assertIs(None, button.getValue())



