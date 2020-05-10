"""Tests for App"""
from generalgui.app import App
import unittest

class AppTest(unittest.TestCase):
    def test_init(self):
        app = App()
        self.assertEqual(app.getChildren(), [])
        self.assertFalse(app.isShown())
        app.show(mainloop=False)
        self.assertTrue(app.isShown())
        app.hide()
        self.assertFalse(app.isShown())




