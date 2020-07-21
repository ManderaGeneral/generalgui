"""Tests for Styler"""

from test.shared_methods import GuiTests

from generalgui import App, Page, Label, Button


class StylerTest(GuiTests):
    def test_init(self):
        page = Page(App())
        label = Label(page, "random")
        page.show(mainloop=False)

        red = label.createStyle("color red", bg="red", priority=3)
        blue = label.createStyle("color blue", bg="blue", priority=2)

        self.assertEqual(False, red.isEnabled())

        blue.enable()
        self.assertEqual("blue", label.getWidgetConfig("bg"))

        blue.disable()
        red.enable()
        self.assertEqual(True, red.isEnabled())
        self.assertEqual("red", label.getWidgetConfig("bg"))

        blue.enable()
        self.assertEqual("red", label.getWidgetConfig("bg"))

        red.disable()
        self.assertEqual(False, red.isEnabled())
        self.assertEqual("blue", label.getWidgetConfig("bg"))

        blue.delete()
        self.assertEqual(False, blue.isEnabled())
        self.assertEqual(red.styleHandler.originalStyle["bg"], label.getWidgetConfig("bg"))

        self.assertRaises(AttributeError, blue.enable)
        self.assertEqual(False, blue.isEnabled())

        self.assertEqual(2, len(label.styleHandler.allStyles))
        self.assertEqual(1, len(label.styleHandler.styles.objects))
        red.enable()
        self.assertEqual(2, len(label.styleHandler.allStyles))
        self.assertEqual(2, len(label.styleHandler.styles.objects))
        red.enable()
        self.assertEqual(2, len(label.styleHandler.allStyles))
        self.assertEqual(2, len(label.styleHandler.styles.objects))

        page.app.remove()

    def test_animate(self):
        pass  # Not working when mainloop is False
        # button = Button(Page(App()), "click here")
        # button.show(mainloop=False)
        #
        # hoverStyle = button.styleHandler.getStyle("Hover")
        # clickStyle = button.styleHandler.getStyle("Click")
        #
        # self.assertEqual(False, hoverStyle.isEnabled())
        # self.assertEqual(False, clickStyle.isEnabled())
        #
        # button.click(animate=True)
        # self.assertEqual(False, hoverStyle.isEnabled())
        # self.assertEqual(True, clickStyle.isEnabled())



















