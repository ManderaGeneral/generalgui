"""Tests for Spreadsheet"""

import unittest

from generalgui import Page, Spreadsheet, Label

import pandas as pd


class SpreadsheetTest(unittest.TestCase):
    def test_init(self):
        columnIndexes = ["col1", "col2"]
        page = Page()
        for cellVSB in range(2):
            for cellHSB in range(2):
                for columnKeys in range(2):
                    for rowKeys in range(2):
                        spreadsheet = Spreadsheet(page, cellVSB=cellVSB, cellHSB=cellHSB, columnKeys=columnKeys, rowKeys=rowKeys)

                        spreadsheet.loadDataFrame(pd.DataFrame([["hello", "there"]], columns=columnIndexes, index=["row"]))

                        if columnKeys:
                            values = [ele.getValue() for ele in spreadsheet.columnKeysGrid.getChildren() if isinstance(ele, Label)]
                            self.assertEqual(columnIndexes, values)
                        else:
                            self.assertIsNone(getattr(spreadsheet, "columnKeysGrid", None))

                        if rowKeys:
                            values = [ele.getValue() for ele in spreadsheet.rowKeysGrid.getChildren()]
                            self.assertEqual(["row"], values)
                        else:
                            self.assertIsNone(getattr(spreadsheet, "rowKeysGrid", None))

                        cellValues = [ele.getValue() for ele in spreadsheet.mainGrid.getChildren() if isinstance(ele, Label)]
                        self.assertEqual(["hello", "there"], cellValues)

        page.app.remove()


