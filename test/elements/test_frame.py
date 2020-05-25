"""Tests for Frame"""

import unittest

from generalgui import Page, Frame


class FrameTest(unittest.TestCase):
    def test_init(self):
        page = Page()
        frame = Frame(page)
        page.show(mainloop=False)

        self.assertEqual(True, frame.isShown())

