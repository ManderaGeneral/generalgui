
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
    def test_draw_page(self):
        page = Page()
        self.draw()
        self.assertEqual(1, page.widget.winfo_ismapped())

    def test_draw_button(self):
        button = Button()
        self.draw()
        self.assertEqual(1, button.widget.winfo_ismapped())

    def test_text(self):
        label = Label(text="hi")
        self.draw()
        self.assertEqual("hi", label.widget["text"])













