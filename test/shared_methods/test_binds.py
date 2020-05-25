"""Tests for binds"""

import unittest

from generalgui import Page, Frame


class FrameTest(unittest.TestCase):
    def test_init(self):
        page = Page()
        frame = Frame(page)
        page.show(mainloop=False)

        # HERE **

