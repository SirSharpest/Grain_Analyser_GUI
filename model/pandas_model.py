import sys
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import pandas as pd


class PandasModel():
    """
    A handle class for pandas to QT dataframe
    """

    def __init__(self, table, dataframe):
        self.df = dataframe
        self.table = table
        self.setup()

    def setup(self):
        self.table.setRowCount(len(self.df))
        self.table.setColumnCount(len(self.df.columns))
        cols = self.df.columns
        self.table.setHorizontalHeaderLabels(cols)
        for idy, row in self.df.iterrows():
            for idx, c in enumerate(cols):
                self.table.setItem(
                    idy, idx, QTableWidgetItem("{0}".format(row[c])))
