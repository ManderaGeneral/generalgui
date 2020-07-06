"""Tests for resizer"""

from test.shared_methods import GuiTests

from generalgui import App, Page, Label


class ResizerTest(GuiTests):
    def test_init(self):
        app = App()
        page = Page(app)
