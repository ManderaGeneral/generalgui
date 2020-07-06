"""Tests for scroller"""

from test.shared_methods import GuiTests

from generalgui import App, Page, Label


class ScrollerTest(GuiTests):
    def test_init(self):
        app = App()
        page = Page(app, width=100, height=100, scrollable=True)
        page2 = Page(page, width=200, height=200)
        page2.show(mainloop=False)
        print(app.getVisibleFraction(page.canvas))

