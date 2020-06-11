"""Tests for Canvas"""

from test.shared_methods import GuiTests

from generalgui import App, Page, Canvas


class CanvasTest(GuiTests):
    def test_init(self):
        page = Page(App())
        canvas = Canvas(page)
        page.show(mainloop=False)

        self.assertEqual(True, canvas.isShown())

