"""Tests for scroller"""

from test.shared_methods import GuiTests

from generalgui import App, Page, Label

from generalvector import Vec2


class ScrollerTest(GuiTests):
    def test_getVisibleFraction(self):
        app = App()
        page = Page(app, width=100, height=100, scrollable=True)
        page2 = Page(page, width=196, height=196)

        with self.assertRaises(AttributeError):
            app.getVisibleFraction(page.canvas)

        page2.show(mainloop=False)
        self.assertEqual(Vec2(0.5), app.getVisibleFraction(page.canvas))

