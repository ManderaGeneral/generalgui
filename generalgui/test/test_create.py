
import unittest

from generalgui import Page, Label, Button

class CreateTest(unittest.TestCase):
    def test_shown(self):
        page = Page()
        self.assertEqual(True, page.shown)
        self.assertEqual(False, page.is_hidden_by_parent())

        label = Label(page, "foo")
        self.assertEqual(True, label.shown)
        self.assertEqual(False, label.is_hidden_by_parent())

        label.shown = False
        self.assertEqual(False, label.shown)
        self.assertEqual(False, label.is_hidden_by_parent())

        page.shown = False
        self.assertEqual(False, page.shown)
        self.assertEqual(False, label.shown)
        self.assertEqual(True, label.is_hidden_by_parent())

        label.shown = True
        self.assertEqual(False, page.shown)
        self.assertEqual(True, label.shown)
        self.assertEqual(True, label.is_hidden_by_parent())


