"""Tests for Page"""

import tkinter as tk

from test.shared_methods import GuiTests

from generalgui import App, Page

from generalvector import Vec2


class PageTest(GuiTests):
    def test_init(self):
        app = App()
        for page in Page(app), Page(app, width=200, height=200):
            self.assertIs(page.parentPage, page.app)
            self.assertIs(page.topElement.parentPage, page)

    def test_siblings(self):
        for page in Page(App()), Page(App(), width=200, height=200):
            self.assertEqual(page.getChildren(), [])
            self.assertEqual(page.getParentPages(), [])
            self.assertEqual(page.getParentPages(includeSelf=True), [page])
            self.assertEqual(page.getTopPage(), page)
            self.assertEqual(page.getSiblings(), [])
            page.showSiblings(mainloop=False)
            page.hideSiblings()
            page.removeSiblings()
            page.show(mainloop=False)
            self.assertTrue(page.isShown())
            page.hide()
            self.assertFalse(page.isShown())
            page.toggleShow(mainloop=False)
            self.assertTrue(page.isShown())
            page.toggleShow(mainloop=False)
            self.assertFalse(page.isShown())

            page3 = Page(page.app)
            page2 = Page(page.app)
            self.assertEqual(page.getSiblings(), [page3, page2])

            page.showSiblings(mainloop=False)
            self.assertTrue(page2.isShown())
            self.assertTrue(page3.isShown())

            page.hideSiblings()
            self.assertFalse(page2.isShown())
            self.assertFalse(page3.isShown())

            page.showSiblings(ignore=page2, mainloop=False)
            self.assertFalse(page2.isShown())
            self.assertTrue(page3.isShown())

            page.hideSiblings(ignore=page3)
            self.assertFalse(page2.isShown())
            self.assertTrue(page3.isShown())

            page.remove()
            self.assertRaises(tk.TclError, page.isShown)

    def test_nextSibling(self):
        page = Page(App())
        page1 = Page(page)
        page2 = Page(page)
        page3 = Page(page)
        self.assertEqual(page1.nextSibling(), page2)
        self.assertEqual(page2.nextSibling(), page3)
        self.assertEqual(page3.nextSibling(), page1)
        self.assertEqual(page3.previousSibling(), page2)
        self.assertEqual(page1.previousSibling(), page3)

    def test_children(self):
        for page in Page(App()), Page(App(), width=200, height=200):
            self.assertEqual(page.getChildren(), [])
            page.showChildren(mainloop=False)
            page.hideChildren()
            page.removeChildren()

            page2 = Page(page)
            self.assertEqual(page.getChildren(), [page2])
            self.assertFalse(page2.isShown())
            page.showChildren(mainloop=False)
            self.assertTrue(page2.isShown())
            page.hideChildren()
            self.assertFalse(page2.isShown())
            page.removeChildren()
            self.assertRaises(tk.TclError, page2.isShown)
            self.assertEqual(page.getChildren(), [])

            page2 = Page(page)
            page3 = Page(page)
            self.assertEqual(page.getChildren(), [page2, page3])
            self.assertEqual(page.getChildren(ignore=page2), [page3])
            self.assertEqual(page.getChildren(ignore=page3), [page2])
            self.assertEqual(page.getChildren(ignore=(page2, page3)), [])
            self.assertEqual(page.getChildren(ignore=[page2, page3]), [])

            self.assertFalse(page2.isShown())
            self.assertFalse(page3.isShown())

            page.showChildren(ignore=(page2, page3), mainloop=False)
            self.assertFalse(page2.isShown())
            self.assertFalse(page3.isShown())

            page.showChildren(ignore=page2, mainloop=False)
            self.assertFalse(page2.isShown())
            self.assertTrue(page3.isShown())

            page.hideChildren()
            self.assertFalse(page2.isShown())
            self.assertFalse(page3.isShown())

            page.showChildren(mainloop=False)
            self.assertTrue(page2.isShown())
            self.assertTrue(page3.isShown())

            page.removeChildren()
            self.assertEqual(page.getChildren(), [])

            page.remove()
            self.assertRaises(tk.TclError, page.isShown)

    def test_parents(self):
        for page in Page(App()), Page(App(), width=200, height=200):
            page2 = Page(page)
            page3 = Page(page2)
            self.assertEqual(page3.getParentPages(), [page2, page])
            self.assertEqual(page3.getParentPages(includeSelf=True), [page3, page2, page])
            self.assertEqual(page3.getTopPage(), page)

            page3.show(mainloop=False)
            self.assertTrue(page3.isShown())
            self.assertTrue(page2.isShown())
            self.assertTrue(page.isShown())
            self.assertTrue(page3.app.isShown())
            self.assertTrue(page2.app.isShown())
            self.assertTrue(page.app.isShown())

    def test_place(self):
        app = App()
        Page(app, width=200, height=200).show(mainloop=False)
        page = Page(app, width=10, height=10, bg="green")
        app.showChildren(mainloop=False)

        page.place(Vec2(100, 100))
        self.assertEqual(Vec2(100, 100), page.getTopLeftPos())

    def test_toggleShow(self):
        app = App()
        page = Page(app)

        self.assertEqual(False, page.isPacked())
        page.toggleShow(mainloop=False)
        self.assertEqual(True, page.isPacked())
        page.toggleShow(mainloop=False)
        self.assertEqual(False, page.isPacked())

    def test_pos(self):
        app = App()
        page = Page(app, width=200, height=100)
        self.assertEqual(Vec2(), page.getTopLeftPos())
        self.assertEqual(Vec2(1), page.getBottomRightPos())
        self.assertEqual(Vec2(1), page.getSize())

        page.show(mainloop=False)
        self.assertEqual(True, page.getWindowPos().inrange(1, 500))
        self.assertEqual(Vec2(200, 100), page.getSize())
        self.assertEqual(Vec2(0), page.getTopLeftPos())
        self.assertEqual(Vec2(200, 100), page.getBottomRightPos())

    def test_states(self):
        app = App()
        page = Page(app)

        self.assertEqual(False, page.isShown())
        self.assertEqual(True, page.exists())
        self.assertEqual(False, page.isPacked())

        page.show(mainloop=False)
        self.assertEqual(True, page.isShown())
        self.assertEqual(True, page.exists())
        self.assertEqual(True, page.isPacked())

        page.hide()
        self.assertEqual(False, page.isShown())
        self.assertEqual(True, page.exists())
        self.assertEqual(False, page.isPacked())

        page.remove()
        self.assertEqual(False, page.isShown(error=False))
        self.assertEqual(False, page.exists())
        self.assertEqual(False, page.isPacked())

















































