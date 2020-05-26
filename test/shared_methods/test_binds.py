"""Tests for binds"""

import unittest

from generalgui import Page, Label


class FrameTest(unittest.TestCase):
    def test_init(self):
        page = Page()
        label = Label(page, "Text")

        bind = label.createBind("<Button-1>", lambda: 5)
        self.assertEqual([5], label.callBind("<Button-1>"))

        label.setBindPropagation("<Button-1>", False)
        self.assertEqual("break", label._bindCaller(True, "<Button-1>"))

        label.removeBind("<Button-1>", bind)
        self.assertEqual("break", label._bindCaller(True, "<Button-1>"))

        label.setBindPropagation("<Button-1>", True)
        self.assertEqual([], label.callBind("<Button-1>"))

        label.createBind("<Button-1>", lambda: 5)
        label.createBind("<Button-1>", lambda: 2)
        self.assertEqual([5, 2], label.callBind("<Button-1>"))

        label.createBind("<Button-1>", lambda: 3, add=False)
        self.assertEqual([3], label.callBind("<Button-1>"))



