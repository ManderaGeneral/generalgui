"""Tests for ElementList"""
from test.shared_methods import GuiTests

from generalgui import App, Page, ElementList, Label, LabelEntry

from generalvector import Vec2


class OptionMenuTest(GuiTests):
    def test_packPart(self):
        elementList = ElementList(Page(App()), maxFirstSteps=5)
        for i in range(6):
            Label(elementList, "hello")
        self.assertEqual([Vec2(0, 0), Vec2(0, 1), Vec2(0, 2), Vec2(0, 3), Vec2(0, 4), Vec2(1, 0)],
                         [elementList.getGridPos(ele) for ele in elementList.getChildren()])

        elementList.removeChildren()
        elementList.maxFirstSteps = 2
        for i in range(6):
            LabelEntry(elementList, "hello")
        self.assertEqual([Vec2(0, 0), Vec2(0, 1), Vec2(1, 0), Vec2(1, 1), Vec2(2, 0), Vec2(2, 1)],
                         [elementList.getGridPos(ele) for ele in elementList.getChildren()])

        # print([elementList.getGridPos(ele) for ele in elementList.getChildren()])


