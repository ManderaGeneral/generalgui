
import unittest
from generalgui import App


class GuiTests(unittest.TestCase):
    def tearDown(self):
        for app in App.getApps():
            app.remove()

