"""Tests for Frame"""

from test.shared_methods import GuiTests

from generalgui import App, Page, Frame


class FrameTest(GuiTests):
    def test_init(self):
        page = Page(App())
        frame = Frame(page)
        page.show(mainloop=False)

        self.assertEqual(True, frame.isShown())

