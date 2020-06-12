"""Tests for Element"""
import tkinter as tk
from test.shared_methods import GuiTests

from generalgui import App, Page, Label, Button, Checkbutton


class ElementTest(GuiTests):
    def test_siblings(self):
        app = App()
        for page in Page(app), Page(app, width=200, height=200):
            text1 = Label(page, "hi")
            text2 = Label(page, "hello")
            self.assertEqual(text1.getSiblings(), [text2])
            self.assertEqual(text2.getSiblings(), [text1])
            self.assertEqual(text1.getSiblings(ignore=text1), [text2])
            self.assertEqual(text1.getSiblings(ignore=text2), [])
            self.assertEqual(text1.getSiblings(ignore=(text1, text2)), [])
            self.assertFalse(text1.isShown())
            self.assertFalse(text2.isShown())

            text1.showSiblings(mainloop=False)
            self.assertTrue(text2.isShown())
            self.assertTrue(text1.isShown())

            text1.hideSiblings(ignore=text2)
            self.assertTrue(text1.isShown())
            self.assertTrue(text2.isShown())

            text1.hideSiblings()
            self.assertTrue(text1.isShown())
            self.assertFalse(text2.isShown())

            text2.removeSiblings()
            self.assertRaises(tk.TclError, text1.isShown)
            self.assertFalse(text2.isShown())

            text1.parentPage.showChildren(mainloop=False)
            self.assertTrue(text2.isShown())

    def test_nextSibling(self):
        page = Page(App())
        button = Button(page, "button")
        label = Label(page, "label")
        checkbutton = Checkbutton(page)
        self.assertEqual(button.nextSibling(), label)
        self.assertEqual(label.nextSibling(), checkbutton)
        self.assertEqual(checkbutton.nextSibling(), button)
        self.assertEqual(checkbutton.previousSibling(), label)
        self.assertEqual(button.previousSibling(), checkbutton)

    def test_children(self):
        app = App()
        for page in Page(app), Page(app, width=200, height=200):
            text1 = Label(page, "hello")
            text2 = Label(page, "there")
            page2 = Page(page)
            text3 = Label(page2, "in page 2")

            # print(page.isScrollable(), page.getChildren())
            self.assertEqual(page.getChildren(), [text1, text2, page2])

            self.assertFalse(text1.isShown())
            self.assertFalse(text2.isShown())
            self.assertFalse(page2.isShown())
            self.assertFalse(text3.isShown())

            page.show(mainloop=False)
            self.assertTrue(text1.isShown())
            self.assertTrue(text2.isShown())

            self.assertFalse(page2.isShown())
            self.assertFalse(text3.isShown())

            page.showChildren(mainloop=False)
            self.assertTrue(page2.isShown())
            self.assertTrue(text3.isShown())

            page.hideChildren()
            self.assertFalse(text1.isShown())
            self.assertFalse(text2.isShown())
            self.assertFalse(page2.isShown())
            self.assertFalse(text3.isShown())

            page.removeChildren()
            self.assertTrue(page.isShown())
            self.assertRaises(tk.TclError, text1.isShown)
            self.assertRaises(tk.TclError, text2.isShown)
            self.assertRaises(tk.TclError, page2.isShown)
            self.assertRaises(tk.TclError, text3.isShown)

    def test_parents(self):
        app = App()
        for page in Page(app), Page(app, width=200, height=200):
            Label(page, "hello")
            Label(page, "there")
            page2 = Page(page)
            text3 = Label(page2, "in page 2")

            self.assertIs(text3.getTopPage(), page)
            self.assertEqual(text3.getParentPages(), [page2, page])
            self.assertEqual(text3.getParentPages(includeSelf=True), [text3, page2, page])

    def test_textOnClick(self):
        text = Label(Page(App()), "hello")
        text.onClick(lambda: 1, add=False)
        self.assertEqual([1], text.click())
        text.onClick(lambda: 2, add=False)
        self.assertEqual([2], text.click())
        text.onClick(lambda: 3, add=True)
        self.assertEqual([2, 3], text.click())
        text.onClick(lambda: 4)
        self.assertEqual([2, 3, 4], text.click())
        text.onClick(lambda: 5, add=False)
        self.assertEqual([5], text.click())

    def test_buttonOnRightClick(self):
        button = Button(Page(App()), "hello")
        button.onRightClick(lambda: 1, add=False)
        self.assertEqual([1], button.rightClick())
        button.onRightClick(lambda: 2, add=False)
        self.assertEqual([2], button.rightClick())
        button.onRightClick(lambda: 3, add=True)
        self.assertEqual([2, 3], button.rightClick())
        button.onRightClick(lambda: 4)
        self.assertEqual([2, 3, 4], button.rightClick())
        button.onRightClick(lambda: 5, add=False)
        self.assertEqual([5], button.rightClick())
































