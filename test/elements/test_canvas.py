"""Tests for Canvas"""

import unittest

from generalgui import App, Page, Canvas


class CanvasTest(unittest.TestCase):
    def test_init(self):
        page = Page(App())
        canvas = Canvas(page)
        page.show(mainloop=False)

        self.assertEqual(True, canvas.isShown())

