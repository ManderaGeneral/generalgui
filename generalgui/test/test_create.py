
import unittest

from generalgui import Page, Label

class CreateTest(unittest.TestCase):
    def test(self):
        label = Label()
        self.assertEqual(True, label.is_shown())
        self.assertEqual(False, label.is_hidden_directly())

        app = label.app
        label.move_to(None)
        self.assertEqual(False, app.widget.is_existing())
