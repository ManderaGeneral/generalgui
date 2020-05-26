"""Tests for Styler"""

import unittest

from generalgui import Page, Label, Button


class StylerTest(unittest.TestCase):
    def test_init(self):
        page = Page()
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

        page.app.remove()

    def test_animate(self):
        pass  # Not working when mainloop is False
        # button = Button(Page(), "click here")
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



















