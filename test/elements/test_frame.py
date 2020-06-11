"""Tests for Frame"""

import unittest

from generalgui import App, Page, Frame


class FrameTest(unittest.TestCase):
    def test_init(self):
        page = Page(App())
        frame = Frame(page)
        page.show(mainloop=False)

        self.assertEqual(True, frame.isShown())

