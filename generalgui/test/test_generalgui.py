
from generalgui import Page
from generallibrary import VerInfo

from unittest import TestCase
import os


class GuiTest(TestCase):
    @classmethod
    def setUpClass(cls):
        if VerInfo().linux:
            os.system('Xvfb :1 -screen 1 1600x1200x16 &')
        os.environ['DISPLAY'] = ':1.0'

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