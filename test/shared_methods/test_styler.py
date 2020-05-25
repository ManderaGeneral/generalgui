"""Tests for Styler"""

import unittest

from generalgui import Page, Label


class StylerTest(unittest.TestCase):
    def test_init(self):
        page = Page()
        label = Label(page, "random")
        page.show(mainloop=False)

        # HERE **

