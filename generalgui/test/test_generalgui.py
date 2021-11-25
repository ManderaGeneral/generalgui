
from generalgui import Page

from unittest import TestCase
import os


class GuiTest(unittest.TestCase):
    def setUpClass(self):
        os.system('Xvfb :1 -screen 0 1600x1200x16  &')
        os.environ['DISPLAY'] = ':1.0'

    def tearDown(self):
        Page.orders.clear()

    @classmethod
    def tearDownClass(cls):
        Page.unreqister_mainloop()

    def draw(self):
        """ Draw everything at once without mainloop. """
        Page.single_loop(limit=0)