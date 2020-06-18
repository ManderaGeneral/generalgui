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

        label = Label(grid, column=0, row=0)
        self.assertEqual(label, grid.getGridElement(Vec2(0, 0)))

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

    def test_fillGrid(self):
        grid = Grid(App())

        self.assertRaises(ValueError, grid.fillGrid, Label, Vec2(0, 0), Vec2(2, 2), values=[1, 2, 3])

        grid.fillGrid(Label, Vec2(0, 0), Vec2(2, 0))
        self.assertEqual([], [grid.getGridPos(ele) for ele in grid.getChildren()])

        grid.fillGrid(Label, Vec2(0, 0), Vec2(0, 0))
        self.assertEqual([], [grid.getGridPos(ele) for ele in grid.getChildren()])

        self.assertRaises(Exception, grid.fillGrid, Label, Vec2(0, 0), Vec2(0, -1))

        grid.fillGrid(Label, Vec2(0, 0), Vec2(2, 1))
        self.assertEqual([Vec2(0, 0), Vec2(1, 0)], [grid.getGridPos(ele) for ele in grid.getChildren()])

        grid.fillGrid(Label, Vec2(0, 0), Vec2(1, 1), removeExcess=True)
        self.assertEqual([Vec2(0, 0)], [grid.getGridPos(ele) for ele in grid.getChildren()])

        grid.fillGrid(Label, Vec2(1, 1), Vec2(1, 1))
        self.assertEqual([Vec2(0, 0), Vec2(1, 1)], [grid.getGridPos(ele) for ele in grid.getChildren()])

        grid.fillGrid(Label, Vec2(0, 0), Vec2(1, 2), removeExcess=True)
        self.assertEqual([Vec2(0, 0), Vec2(0, 1)], [grid.getGridPos(ele) for ele in grid.getChildren()])

        grid.fillGrid(Label, Vec2(1, 0), Vec2(2, 2), removeExcess=True)
        self.assertEqual([Vec2(0, 0), Vec2(0, 1), Vec2(1, 0), Vec2(2, 0), Vec2(1, 1), Vec2(2, 1)],
                         [grid.getGridPos(ele) for ele in grid.getChildren()])

    def test_getFirstElementPos(self):
        grid = Grid(App())

        Label(grid, column=1, row=2)

        # Ints sanitize
        self.assertRaises(Exception, grid.getFirstElementPos, Vec2(1, 0.5))

        # Initial jump
        self.assertEqual(None, grid.getFirstElementPos(Vec2(-1, 0), Vec2(1, 1)))
        self.assertEqual(Vec2(1.0, 2), grid.getFirstElementPos(Vec2(1, -1)))
        self.assertEqual(Vec2(1, 2), grid.getFirstElementPos(Vec2(-1, 0), Vec2(1, 1), confine=True))

        # Initial jump with max steps
        self.assertEqual(None, grid.getFirstElementPos(Vec2(-1, 0), Vec2(1, 1), confine=True, maxSteps=1))
        self.assertEqual(Vec2(1, 2), grid.getFirstElementPos(Vec2(-1, 0), Vec2(1, 1), confine=True, maxSteps=2))

        # No initial jump, then three jumps
        self.assertEqual(None, grid.getFirstElementPos(Vec2(0, 0), Vec2(1, 1)))
        self.assertEqual(Vec2(1, 2), grid.getFirstElementPos(Vec2(0, 0), Vec2(1, 1), confine=True))

        # No jumps, move two steps
        self.assertEqual(Vec2(1, 2), grid.getFirstElementPos(Vec2(1, 0), Vec2(0, 1)))
        self.assertEqual(None, grid.getFirstElementPos(Vec2(1, 0), Vec2(0, 1), maxSteps=1))

        # Two elements in row, make sure it gets first
        Label(grid, column=2, row=2)
        self.assertEqual(Vec2(1, 2), grid.getFirstElementPos(Vec2(0, 2), Vec2(1, 0)))

        # Step over one element
        self.assertEqual(Vec2(2, 2), grid.getFirstElementPos(Vec2(0, 2), Vec2(2, 0)))

        # Jump with multiple elements
        self.assertEqual(None, grid.getFirstElementPos(Vec2(0, 2), Vec2(-1, 0)))
        self.assertEqual(Vec2(2, 2), grid.getFirstElementPos(Vec2(0, 2), Vec2(-1, 0), confine=True))

        # Initial jump with multiple elements
        Label(grid, column=0, row=2)
        self.assertEqual(Vec2(0, 2), grid.getFirstElementPos(Vec2(3, 2), Vec2(1, 0)))

    def test_getFirstEmptyPos(self):
        grid = Grid(App())

        # Simple column with empty grid
        self.assertEqual(Vec2(1, 0), grid.getFirstEmptyPos(Vec2(1, 0), Vec2(0, 1)))
        self.assertEqual(Vec2(1, 0), grid.getFirstEmptyPos(Vec2(1, -1), Vec2(0, -1)))
        self.assertEqual(Vec2(1, 0), grid.getFirstEmptyPos(Vec2(1, 0)))
        self.assertEqual(Vec2(1, 0), grid.getFirstEmptyPos(Vec2(1, -1)))

        Label(grid, column=1, row=1)
        # From top of column going down
        self.assertEqual(Vec2(1, 0), grid.getFirstEmptyPos(Vec2(1, 0), Vec2(0, 1)))
        # From bottom of column going up, over label
        self.assertEqual(Vec2(1, 0), grid.getFirstEmptyPos(Vec2(1, -1), Vec2(0, -1)))
        # From bottom of column going down without confine
        self.assertEqual(None, grid.getFirstEmptyPos(Vec2(1, 1), Vec2(0, 1)))
        # From bottom of column going down with confine
        self.assertEqual(Vec2(1, 0), grid.getFirstEmptyPos(Vec2(1, 1), Vec2(0, 1), confine=True))

    def test_getFirstPatternPos(self):
        grid = Grid(App())
        self.assertEqual(Vec2(0, 0), pos := grid.getFirstPatternPos())
        Label(grid, pos=pos)
        self.assertEqual(Vec2(0, 1), pos := grid.getFirstPatternPos())
        Label(grid, pos=pos)
        self.assertEqual(Vec2(0, 2), pos := grid.getFirstPatternPos())
        Label(grid, pos=pos)
        self.assertEqual(Vec2(0, 3), pos := grid.getFirstPatternPos())
        Label(grid, pos=pos)
        self.assertEqual(Vec2(0, 4), pos := grid.getFirstPatternPos())
        Label(grid, pos=pos)
        self.assertEqual(Vec2(1, 0), pos := grid.getFirstPatternPos())
        Label(grid, pos=pos)
        self.assertEqual(Vec2(1, 1), pos := grid.getFirstPatternPos())
        Label(grid, pos=pos)

        # HERE  ** A few more tests!


    def test_append(self):
        grid = Grid(App())
        # Column 2
        self.assertEqual(Vec2(2, 0), grid.appendToColumn(Label(grid, pack=False), 2))
        self.assertEqual(Vec2(2, 1), grid.appendToColumn(Label(grid, pack=False), 2))
        # Column 1
        self.assertEqual(Vec2(1, 0), grid.appendToColumn(Label(grid, pack=False), 1))

        # Row 0
        self.assertEqual(Vec2(0, 0), grid.appendToRow(Label(grid, pack=False), 0))
        self.assertEqual(Vec2(3, 0), grid.appendToRow(Label(grid, pack=False), 0))
        self.assertEqual(Vec2(4, 0), grid.appendToRow(Label(grid, pack=False), 0))

        # Row 1
        self.assertEqual(Vec2(0, 1), grid.appendToRow(Label(grid, pack=False), 1))
        self.assertEqual(Vec2(1, 1), grid.appendToRow(Label(grid, pack=False), 1))

        # Column 0
        self.assertEqual(Vec2(0, 2), grid.appendToColumn(Label(grid, pack=False), 0))






































