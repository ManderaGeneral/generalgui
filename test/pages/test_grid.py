"""Tests for Grid"""
from test.shared_methods import GuiTests

from generalgui import App, Grid, ElementList, Label, LabelEntry

from generalvector import Vec2


class OptionMenuTest(GuiTests):
    def test_getGridElement(self):
        grid = Grid(App())
        self.assertEqual(None, grid.getGridElement(Vec2(1, 0)))

        label = Label(grid, "hello", column=1, row=0)
        self.assertEqual(label, grid.getGridElement(Vec2(1, 0)))

    def test_getGridPos(self):
        grid = Grid(App())

        label = Label(Grid(App()), "hello")
        self.assertRaises(AttributeError, grid.getGridPos, label)

        label = Label(grid, "hello", column=1, row=1, pack=False)
        self.assertRaises(AttributeError, grid.getGridPos, label)

        label.pack()
        self.assertEqual(Vec2(1, 1), grid.getGridPos(label))

    def test_getGridSize(self):
        grid = Grid(App())
        self.assertEqual(Vec2(0, 0), grid.getGridSize())

        label1 = Label(grid, "hello", column=1, row=0)
        self.assertEqual(Vec2(2, 1), grid.getGridSize())

        label2 = Label(grid, "hello", column=2, row=1)
        self.assertEqual(Vec2(3, 2), grid.getGridSize())

        label2.remove()
        self.assertEqual(Vec2(2, 1), grid.getGridSize())

        label1.remove()
        self.assertEqual(Vec2(0, 0), grid.getGridSize())



