
import unittest

from generalgui import Page, Label, Button


class GuiTest(unittest.TestCase):
    def tearDown(self):
        Page.orders.clear()

    @classmethod
    def tearDownClass(cls):
        Page.unreqister_mainloop()

    def draw(self):
        """ Draw everything at once without mainloop. """
        Page.single_loop(limit=0)

class CreateTest(GuiTest):
    def test_draw(self):
        page = Page()

        self.draw()

        print(page.widget.winfo_ismapped())

