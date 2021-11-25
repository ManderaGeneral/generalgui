
from generalgui import Page

from unittest import TestCase
import os


class GuiTest(TestCase):
    @classmethod
    def setUpClass(cls):
        # os.system('Xvfb :2 -screen 0 1600x1200x16  &')
        os.environ['DISPLAY'] = ':0.0'

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        Page.unreqister_mainloop()

    def tearDown(self):
        Page.orders.clear()

    def draw(self):
        """ Draw everything at once without mainloop. """
        Page.single_loop(limit=0)