"""Tests for App"""
from generalgui.page import Page
from generalgui.element import Text, Button
from generalgui.dropdown import Dropdown

import unittest
import tkinter as tk

class ElementTest(unittest.TestCase):
    def test_text(self):
        for page in Page(), Page(width=200):
            text = Text(page, "hello")
            self.assertEqual(text.parentPage, page)
            self.assertIs(text.widget.element, text)
            self.assertFalse(text.isShown())

            text.show(mainloop=False)
            self.assertTrue(text.isShown())

            page.app.remove()
            self.assertRaises(tk.TclError, text.isShown)

    def test_button(self):
        for page in Page(), Page(width=200):
            button = Button(page, "hello", lambda: 5)
            self.assertEqual(button.parentPage, page)
            self.assertIs(button.widget.element, button)
            self.assertFalse(button.isShown())

            button.show(mainloop=False)
            self.assertTrue(button.isShown())

            self.assertEqual(button.click(), 5)

            page.app.remove()
            self.assertRaises(tk.TclError, button.isShown)

    def test_siblings(self):
        for page in Page(), Page(width=200):
            text1 = Text(page, "hi")
            text2 = Text(page, "hello")
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
            page.app.remove()

    def test_children(self):
        for page in Page(), Page(width=200):
            text1 = Text(page, "hello")
            text2 = Text(page, "there")
            page2 = Page(page)
            text3 = Text(page2, "in page 2")

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

            page.app.remove()

    def test_parents(self):
        for page in Page(), Page(width=200):
            Text(page, "hello")
            Text(page, "there")
            page2 = Page(page)
            text3 = Text(page2, "in page 2")

            self.assertIs(text3.getTopPage(), page)
            self.assertEqual(text3.getParentPages(), [page2, page])
            self.assertEqual(text3.getParentPages(includeSelf=True), [text3, page2, page])

    def test_textOnClick(self):
        text = Text(Page(), "hello")
        text.onClick(lambda: 1)
        self.assertEqual(text.click(), 1)
        text.onClick(lambda: 2)
        self.assertEqual(text.click(), 2)
        text.onClick(lambda: 3, add=True)
        self.assertEqual(text.click(), (2, 3))
        text.onClick(lambda: 4, add=True)
        self.assertEqual(text.click(), (2, 3, 4))
        text.onClick(lambda: 5)
        self.assertEqual(text.click(), 5)

    def test_buttonOnRightClick(self):
        button = Button(Page(), "hello")
        button.onRightClick(lambda: 1)
        self.assertEqual(button.rightClick(), 1)
        button.onRightClick(lambda: 2)
        self.assertEqual(button.rightClick(), 2)
        button.onRightClick(lambda: 3, add=True)
        self.assertEqual(button.rightClick(), (2, 3))
        button.onRightClick(lambda: 4, add=True)
        self.assertEqual(button.rightClick(), (2, 3, 4))
        button.onRightClick(lambda: 5)
        self.assertEqual(button.rightClick(), 5)
































