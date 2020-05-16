"""Tests for Spreadsheet"""

import unittest

from generalgui import Page, Spreadsheet


class SpreadsheetTest(unittest.TestCase):
    def test(self):
        spreadsheet = Spreadsheet(Page())

        spreadsheet.addRows(["hello", "there"])

        spreadsheet.app.remove()


