"""Tests for App"""
from generalgui.app import App
from generalgui.page import Page

import unittest
import tkinter as tk


class AppTest(unittest.TestCase):
    def test_init(self):
        app = App()
        self.assertIsNone(app.parentPage)
        self.assertIs(app.app, app)
        self.assertTrue(isinstance(app.widget, tk.Tk))
        self.assertIs(app.widget.element, app)

        self.assertEqual(app.getChildren(), [])
        self.assertFalse(app.isShown())
        app.show(mainloop=False)
        self.assertTrue(app.isShown())
        app.hide()
        self.assertFalse(app.isShown())
        app.remove()
        self.assertRaises(tk.TclError, app.isShown)

    def test_children(self):
        app = App()
        self.assertEqual(app.getChildren(), [])
        app.showChildren()
        app.hideChildren()
        app.removeChildren()

        page = Page(app)
        self.assertEqual(app.getChildren(), [page])
        self.assertFalse(page.isShown())
        app.showChildren(mainloop=False)
        self.assertTrue(page.isShown())
        app.hideChildren()
        self.assertFalse(page.isShown())
        app.removeChildren()
        self.assertRaises(tk.TclError, page.isShown)
        self.assertEqual(app.getChildren(), [])


        page = Page(app)
        page2 = Page(app)
        self.assertEqual(app.getChildren(), [page, page2])
        self.assertEqual(app.getChildren(ignore=page), [page2])
        self.assertEqual(app.getChildren(ignore=page2), [page])
        self.assertEqual(app.getChildren(ignore=(page, page2)), [])

        self.assertFalse(page.isShown())
        self.assertFalse(page2.isShown())

        app.showChildren(ignore=(page, page2), mainloop=False)
        self.assertFalse(page.isShown())
        self.assertFalse(page2.isShown())

        app.showChildren(ignore=page, mainloop=False)
        self.assertFalse(page.isShown())
        self.assertTrue(page2.isShown())

        app.hideChildren()
        self.assertFalse(page.isShown())
        self.assertFalse(page2.isShown())

        app.showChildren(mainloop=False)
        self.assertTrue(page.isShown())
        self.assertTrue(page2.isShown())

        app.removeChildren()
        self.assertEqual(app.getChildren(), [])


        page = Page(app)
        page2 = Page(page)

        page2.show(mainloop=False)
        self.assertTrue(page.isShown())

        page.hideChildren()
        self.assertFalse(page2.isShown())

        page2.show(mainloop=False)
        self.assertTrue(page2.isShown())




