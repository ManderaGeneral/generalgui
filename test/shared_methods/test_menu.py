"""Tests for menu"""

from test.shared_methods import GuiTests

from generalgui import App, Page, Label


class MenuTest(GuiTests):
    def test_init(self):
        app = App()
        page = Page(app)
        page.menu("testing", return_5=lambda: 5)

        page.showMenu()
        self.assertEqual(True, app.menuPage.getElementByValue("testing") is not None)
        self.assertEqual([5], app.menuPage.getElementByValue("return 5").click(animate=False))
        self.assertEqual(None, app.menuPage)
        page.showMenu()
        self.assertEqual(True, app.menuPage is not None)
        page.hideMenu()
        self.assertEqual(None, app.menuPage)

        label = Label(page, "label text here")
        label.menu("labels menu", **{"info:": lambda: 2, "btn": lambda: True})

        page.showMenu()
        self.assertEqual(True, app.menuPage.getElementByValue("testing") is not None)
        self.assertEqual(None, app.menuPage.getElementByValue("labels menu"))
        self.assertEqual(None, app.menuPage.getElementByValue("info: 2"))
        self.assertEqual(None, app.menuPage.getElementByValue("btn"))
        self.assertEqual([5], app.menuPage.getElementByValue("return 5").click(animate=False))

        label.showMenu()
        self.assertEqual(True, app.menuPage.getElementByValue("testing") is not None)
        self.assertEqual(True, app.menuPage.getElementByValue("labels menu") is not None)
        self.assertEqual(True, app.menuPage.getElementByValue("info: 2") is not None)
        self.assertEqual([True], app.menuPage.getElementByValue("btn").click(animate=False))









