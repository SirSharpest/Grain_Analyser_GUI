from PyQt5.QtWidgets import QRadioButton, QComboBox
from matplotlib_canvas_model import MyStaticMplCanvas
from pandas.api.types import is_numeric_dtype
import numpy as np


class MatplotlibCanvasView():
    def __init__(self, df, parent_layout, plot_layout, settings_layout, plot_type):
        """
        Given a dataframe and a layout spec
        this class populates appropriate radio button functionality
        """
        self.df = df
        self.parent_layout = parent_layout
        self.settings_layout = settings_layout
        self.plot_type = plot_type
        self.buttons = {}
        offset = 0
        for idx, c in enumerate(df.columns):
            tmp_btn = QRadioButton(c)
            if len(self.buttons) == 0:
                tmp_btn.setChecked(True)
            else:
                tmp_btn.setChecked(False)
            if not is_numeric_dtype(df[c]):
                offset = offset + 1
                continue
            tmp_btn.column = c
            self.buttons[c] = tmp_btn
            offset_num = idx - offset
            self.settings_layout.addWidget(
                self.buttons[c], offset_num % 2, offset_num // 2)

        if self.plot_type == 'boxplot':
            self.cb_group_by = QComboBox()
            [self.cb_group_by.addItem(x)
             for x in self.find_candidates_for_box_plots(self.df)]
            self.settings_layout.addWidget(self.cb_group_by, 2, 0)

    def find_candidates_for_box_plots(self, df):
        lst = []
        for c in df.columns:
            if len(df[c].unique()) < 30:
                lst.append(c)
        return lst

    def get_cb_group_by(self):
        return self.cb_group_by

    def get_radio_buttons(self):
        # Returns a dict of the radio buttons created
        return self.buttons
