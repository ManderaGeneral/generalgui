"""Tests for App"""

import tkinter as tk

from test.shared_methods import GuiTests

from generalgui import App, Page

from generallibrary.time import sleep


class AppTest(GuiTests):
    def test_init(self):
        app = App()
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
        self.assertEqual(False, app.isShown(error=False))

    def test_children(self):
        app = App()
        self.assertEqual(app.getChildren(), [])
        app.showChildren(mainloop=False)
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


        page = Page(app, height=200)
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


        page = Page(app, width=200)
        page2 = Page(page)

        page2.show(mainloop=False)
        self.assertTrue(page.isShown())

        page.hideChildren()
        self.assertFalse(page2.isShown())

        page2.show(mainloop=False)
        self.assertTrue(page2.isShown())

    def test_after(self):
        app = App()
        self.assertEqual({}, app.afters)

        one = app.widget.after(500, lambda: 5)
        self.assertEqual({0: "after#0"}, app.afters)

        two = app.widget.after(500, lambda: 5)
        self.assertEqual({0: "after#0", 1: "after#1"}, app.afters)

        app.widget.after_cancel(one)
        self.assertEqual({1: "after#1"}, app.afters)

        three = app.widget.after(500, lambda: print(5))
        self.assertEqual({0: "after#2", 1: "after#1"}, app.afters)

        app.widget.after_cancel(two)
        app.widget.after_cancel(three)
        self.assertEqual({}, app.afters)

    def test_apps(self):
        self.assertEqual([], App.getApps())

        app = App()
        self.assertEqual([app], app.getApps())

        app2 = App()
        self.assertEqual([app, app2], app.getApps())
        self.assertEqual([app, app2], App.getApps())

        app.remove()
        self.assertEqual([app2], App.getApps())

        app2.remove()
        self.assertEqual([], App.getApps())

    # HERE ** Go through all shared methods that app have
























