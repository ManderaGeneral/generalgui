"""Tests for App"""

import tkinter as tk

from test.shared_methods import GuiTests

from generalgui import App, Page, LabelEntry, Button

from generallibrary.time import sleep

from generalvector import Vec2


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

        self.assertEqual([page, page2], app.getChildren(recurrent=True))
        labelEntry = LabelEntry(page2)
        self.assertEqual([page, page2, labelEntry, labelEntry.label, labelEntry.entry], app.getChildren(recurrent=True))

    def test_after(self):
        app = App()
        self.assertEqual({}, app.afters)

        one = app.widget.after(500, lambda: 5)
        self.assertEqual([0], list(app.afters.keys()))

        two = app.widget.after(500, lambda: 5)
        self.assertEqual([0, 1], list(app.afters.keys()))

        app.widget.after_cancel(one)
        self.assertEqual([1], list(app.afters.keys()))

        three = app.widget.after(500, lambda: print(5))
        self.assertEqual([1, 0], list(app.afters.keys()))

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

    def test_pos(self):
        app = App()
        self.assertEqual(Vec2(), app.getWindowPos())
        self.assertEqual(Vec2(1), app.getSize())
        app.show(mainloop=False)
        self.assertEqual(True, app.getWindowPos().inrange(1, 500))

        self.assertEqual(Vec2(), app.getTopLeftPos())
        self.assertEqual(Vec2(200), app.getBottomRightPos())
        self.assertEqual(Vec2(200), app.getSize())

        app.setSize(Vec2(250, 300))
        app.widget.update()
        self.assertEqual(Vec2(250, 300), app.getSize())

        app.setSize(145)
        app.widget.update()
        self.assertEqual(Vec2(145), app.getSize())

        page = Page(app, width=300, height=250)
        page.show(mainloop=False)
        self.assertEqual(Vec2(300, 250), app.getBottomRightPos())
        self.assertEqual(Vec2(300, 250), app.getSize())

        self.assertEqual(True, app.getMouse().inrange(-100000, 100000))

        self.assertEqual(page.frame, app.getElementByPos(10))

        page.remove()
        self.assertEqual(app, app.getElementByPos(10))

        self.assertEqual(None, app.getElementByPos(-10))
        self.assertEqual(None, app.getElementByPos(400))

    def test_rainbow(self):
        app = App()

        labelEntry = LabelEntry(Page(app))
        self.assertEqual(None, labelEntry.label.styleHandler)

        app.rainbow()
        self.assertEqual(["Original", "Rainbow"], list(labelEntry.label.styleHandler.allStyles.keys()))
        self.assertEqual(True, labelEntry.label.styleHandler.getStyle("Rainbow").isEnabled())

        self.assertEqual(["Original", "Hover", "Click", "Rainbow"], list(labelEntry.entry.styleHandler.allStyles.keys()))
        self.assertEqual(True, labelEntry.entry.styleHandler.getStyle("Rainbow").isEnabled())

        self.assertEqual(["Original", "Rainbow"], list(app.getChildren()[0].frame.styleHandler.allStyles.keys()))
        self.assertEqual(True, app.getChildren()[0].frame.styleHandler.getStyle("Rainbow").isEnabled())

        app.rainbow(reset=True)
        self.assertEqual(False, labelEntry.label.styleHandler.getStyle("Rainbow").isEnabled())
        self.assertEqual(False, labelEntry.entry.styleHandler.getStyle("Rainbow").isEnabled())
        self.assertEqual(False, app.getChildren()[0].frame.styleHandler.getStyle("Rainbow").isEnabled())

    def test_getParents(self):
        app = App()
        LabelEntry(Page(app))

        self.assertEqual([], app.getParents())
        self.assertEqual([app], app.getParents(includeSelf=True))
        self.assertEqual([app], app.getParents(includeApp=True))
        self.assertEqual([app], app.getParents(includeSelf=True, includeApp=True))

    def test_getFirstParentByClass(self):
        app = App()
        LabelEntry(Page(app))

        self.assertEqual(None, app.getFirstParentByClass("App"))
        self.assertEqual(app, app.getFirstParentByClass("App", includeSelf=True))
        self.assertEqual(None, app.getFirstParentByClass("LabelEntry", includeSelf=True))

    def test_getBaseTopElementWidget(self):
        app = App()
        LabelEntry(Page(app))

        self.assertEqual(app, app.getBaseElement())
        self.assertEqual(app.widget, app.getBaseWidget())

        self.assertEqual(app, app.getTopElement())
        self.assertEqual(app.widget, app.getTopWidget())

    def test_states(self):
        app = App()

        self.assertEqual(False, app.isShown())
        self.assertEqual(True, app.exists())
        self.assertEqual(True, app.isPacked())

        app.show(mainloop=False)
        self.assertEqual(True, app.isShown())
        self.assertEqual(True, app.exists())
        self.assertEqual(True, app.isPacked())

        app.hide()
        self.assertEqual(False, app.isShown())
        self.assertEqual(True, app.exists())
        self.assertEqual(True, app.isPacked())

        app.remove()
        self.assertEqual(False, app.isShown())
        self.assertEqual(False, app.exists())
        self.assertEqual(False, app.isPacked())

    def test_config(self):
        app = App()
        self.assertEqual(True, "bg" in app.getAllWidgetConfigs())
        self.assertEqual("SystemButtonFace", app.getWidgetConfig("bg"))

        app.widgetConfig(bg="red")
        self.assertEqual("red", app.getWidgetConfig("bg"))

        with self.assertRaises(tk.TclError):
            app.getWidgetConfig("doesntexist")

    def test_getElementByValue(self):
        app = App()

        labelEntry = LabelEntry(Page(app), value="value here")
        self.assertEqual(labelEntry.label, app.getElementByValue("value here"))

        button = Button(Page(Page(Page(app))), value="test val")
        self.assertEqual(button, app.getElementByValue("test val"))




















