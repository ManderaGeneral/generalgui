"""Tests for App"""
from generalgui.page import Page
from generalgui.element import Text

import unittest
import tkinter as tk


class PageTest(unittest.TestCase):
    def test_init(self):
        page = Page()
        text = Text(page, "hello")
        self.assertEqual(text.parentPage, page)
        self.assertEqual(text.widget, page)
        self.assertEqual(text.side, "top")

    def test_siblings(self):
        pass

    def test_children(self):
        pass

    def test_parents(self):
        pass
















































