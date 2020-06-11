"""Tests for Scrollbar"""

from test.shared_methods import GuiTests

from generalgui import App, Page, Scrollbar


class ScrollbarTest(GuiTests):
    def test_init(self):
        page = Page(App())
        scrollbar = Scrollbar(page)
        page.show(mainloop=False)

        self.assertEqual(True, scrollbar.isShown())

