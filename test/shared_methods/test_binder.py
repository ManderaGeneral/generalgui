"""Tests for binds"""

from test.shared_methods import GuiTests

from generalgui import App, Page, Label


class BinderTest(GuiTests):
    def test_init(self):
        page = Page(App())
        label = Label(page, "Text")

        bind = label.createBind("<Button-1>", lambda: 5)
        self.assertEqual([5], label.callBind("<Button-1>"))

        bind.remove()
        self.assertEqual([], label.callBind("<Button-1>"))

        label.createBind("<Button-1>", lambda: 5)
        page.createBind("<Button-1>", lambda: 2)
        self.assertEqual([5, 2], label.callBind("<Button-1>"))

        label.setBindPropagation("<Button-1>", False)
        self.assertEqual([5], label.callBind("<Button-1>"))

        label.setBindPropagation("<Button-1>", True)
        self.assertEqual([5, 2], label.callBind("<Button-1>"))

        label.setBindPropagation("<Button-1>", False)
        label.createBind("<Button-1>", lambda: 5)
        label.createBind("<Button-1>", lambda: 2)
        self.assertEqual([5, 5, 2], label.callBind("<Button-1>"))

        label.createBind("<Button-1>", lambda: 3, add=False)
        self.assertEqual([3], label.callBind("<Button-1>"))

        label.createBind("<Button-1>", lambda: 5, name="hello")
        self.assertEqual([3, 5], label.callBind("<Button-1>"))

        label.createBind("<Button-1>", lambda: 5, name="hello")
        self.assertEqual([3, 5], label.callBind("<Button-1>"))

        label.createBind("<Button-1>", lambda: 5, name="hello", add=False)
        self.assertEqual([5], label.callBind("<Button-1>"))

        label.onClick(lambda: 5, add=False)
        label.onClick(lambda: 2)
        self.assertEqual([5, 2], label.click(animate=False))
        self.assertEqual([5, 2], label.click(animate=True))

        label.onRightClick(lambda: 5, add=False)
        label.onRightClick(lambda: 2)
        self.assertEqual([5, 2], label.rightClick(animate=False))
        self.assertEqual([5, 2], label.rightClick(animate=True))

        label.remove()
        self.assertEqual([], label.callBind("<Button-1>"))





