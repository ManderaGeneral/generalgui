"""Tests for menu"""

from test.shared_methods import GuiTests

from generalgui import App, Page, Label


class MenuTest(GuiTests):
    def test_init(self):
        app = App()
        page = Page(app)
        page.menu("testing", return_5=lambda: 5)

        page.showMenu()
        self.assertEqual([5], app.menuPage.getElementByValue("return 5").click())
