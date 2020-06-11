"""Tests for Scrollbar"""

import unittest

from generalgui import App, Page, Scrollbar


class ScrollbarTest(unittest.TestCase):
    def test_init(self):
        page = Page(App())
        scrollbar = Scrollbar(page)
        page.show(mainloop=False)

        self.assertEqual(True, scrollbar.isShown())

