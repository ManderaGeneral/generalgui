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
                        spreadsheet.loadDataFrame(pd.DataFrame([["foo", 5], ["bar", 2.2]], columns=["name", "number"], index=["row", "another"]))

                        if columnKeys:
                            values = [ele.getValue() for ele in spreadsheet.columnKeysGrid.getChildren() if isinstance(ele, Label)]
                            self.assertEqual(["name", "number"], values)
                        else:
                            self.assertIsNone(getattr(spreadsheet, "columnKeysGrid", None))

                        if rowKeys:
                            values = [ele.getValue() for ele in spreadsheet.rowKeysGrid.getChildren()]
                            self.assertEqual(["row", "another"], values)
                        else:
                            self.assertIsNone(getattr(spreadsheet, "rowKeysGrid", None))

                        cellValues = [ele.getValue() for ele in spreadsheet.mainGrid.getChildren() if isinstance(ele, Label)]  # Left to right, row by row
                        self.assertEqual(["foo", 5, "bar", 2.2], cellValues)

                        spreadsheet.sortIndex()
                        cellValues = [ele.getValue() for ele in spreadsheet.mainGrid.getChildren() if isinstance(ele, Label)]  # Left to right, row by row
                        self.assertEqual(["bar", 2.2, "foo", 5], cellValues)

                        spreadsheet.sortHeader()
                        cellValues = [ele.getValue() for ele in spreadsheet.mainGrid.getChildren() if isinstance(ele, Label)]  # Left to right, row by row
                        self.assertEqual(["bar", 2.2, "foo", 5], cellValues)

                        spreadsheet.sortHeader()
                        cellValues = [ele.getValue() for ele in spreadsheet.mainGrid.getChildren() if isinstance(ele, Label)]  # Left to right, row by row
                        self.assertEqual([2.2, "bar", 5, "foo"], cellValues)

                        spreadsheet.sortIndex()
                        cellValues = [ele.getValue() for ele in spreadsheet.mainGrid.getChildren() if isinstance(ele, Label)]  # Left to right, row by row
                        self.assertEqual([5, "foo", 2.2, "bar"], cellValues)



