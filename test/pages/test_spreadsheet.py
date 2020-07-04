"""Tests for Spreadsheet"""

from test.shared_methods import GuiTests

from generalgui import App, Page, Spreadsheet, Label

import pandas as pd


class SpreadsheetTest(GuiTests):
    def test_init(self):
        page = Page(App())
        for cellVSB in range(2):
            for cellHSB in range(2):
                for columnKeys in range(2):
                    for rowKeys in range(2):
                        spreadsheet = Spreadsheet(page, cellVSB=cellVSB, cellHSB=cellHSB, columnKeys=columnKeys, rowKeys=rowKeys)

                        # Named keys
                        spreadsheet.loadDataFrame(pd.DataFrame([["foo", 5], ["bar", 2.2]], columns=["col_a", "col_b"], index=["row_a", "row_b"]))
                        self.assertEqual(["foo", 5, "bar", 2.2], spreadsheet.getMainValues())

                        if columnKeys:
                            self.assertEqual(["col_a", "col_b"], spreadsheet.getHeaderValues())
                        else:
                            self.assertIsNone(getattr(spreadsheet, "headerGrid", None))

                        if rowKeys:
                            self.assertEqual(["row_a", "row_b"], spreadsheet.getIndexValues())
                        else:
                            self.assertIsNone(getattr(spreadsheet, "indexGrid", None))

                        spreadsheet.sortIndex()
                        self.assertEqual(["foo", 5,
                                          "bar", 2.2], spreadsheet.getMainValues())
                        self.assertEqual(["col_a", "col_b"], spreadsheet.getHeaderValues())
                        self.assertEqual(["row_a", "row_b"], spreadsheet.getIndexValues())

                        spreadsheet.sortHeader()
                        self.assertEqual(["foo", 5,
                                          "bar", 2.2], spreadsheet.getMainValues())
                        self.assertEqual(["col_a", "col_b"], spreadsheet.getHeaderValues())
                        self.assertEqual(["row_a", "row_b"], spreadsheet.getIndexValues())

                        spreadsheet.sortHeader()
                        self.assertEqual([5, "foo",
                                          2.2, "bar"], spreadsheet.getMainValues())
                        self.assertEqual(["col_b", "col_a"], spreadsheet.getHeaderValues())
                        self.assertEqual(["row_a", "row_b"], spreadsheet.getIndexValues())

                        spreadsheet.sortIndex()
                        self.assertEqual([2.2, "bar",
                                          5, "foo"], spreadsheet.getMainValues())
                        self.assertEqual(["col_b", "col_a"], spreadsheet.getHeaderValues())
                        self.assertEqual(["row_b", "row_a"], spreadsheet.getIndexValues())

                        spreadsheet.makeRowHeader("row_a")
                        self.assertEqual(["col_b", "col_a",
                                          2.2, "bar"], spreadsheet.getMainValues())
                        self.assertEqual([5, "foo"], spreadsheet.getHeaderValues())
                        self.assertEqual(["headers", "row_b"], spreadsheet.getIndexValues())

