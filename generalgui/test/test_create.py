
from generalgui import Page, Label
from generalgui.test.test_generalgui import GuiTest


class CreateTest(GuiTest):
    def test_shown(self):
        page = Page()
        self.assertEqual(True, page.shown)
        self.assertEqual(False, page.is_hidden_by_parent())

        label = Label(page, "foo")
        self.assertEqual(True, label.shown)
        self.assertEqual(False, label.is_hidden_by_parent())

        label.shown = False
        self.assertEqual(False, label.shown)
        self.assertEqual(False, label.is_hidden_by_parent())

        page.shown = False
        self.assertEqual(False, page.shown)
        self.assertEqual(False, label.shown)
        self.assertEqual(True, label.is_hidden_by_parent())

        label.shown = True
        self.assertEqual(False, page.shown)
        self.assertEqual(True, label.shown)
        self.assertEqual(True, label.is_hidden_by_parent())

    def test_values(self):
        label = Label(None, "hi")
        self.assertEqual("hi", label.text)
        label.text = "foo"
        self.assertEqual("foo", label.text)
        label.text = None
        self.assertEqual("", label.text)

    def test_contain(self):
        with self.assertRaises(Exception):
            Label(Label())
        Page(Page())

    def test_binder(self):
        label = Label()
        label.bind(lambda: 5)
        self.assertEqual((5, ), label.call_binds())
        label.bind(lambda: "hi")
        self.assertEqual((5, "hi"), label.call_binds())
















