from PyQt5.QtWidgets import QRadioButton
from matplotlib_canvas_model import MyStaticMplCanvas
from pandas.api.types import is_numeric_dtype


class MatplotlibCanvasView():
    def __init__(self, df, parent_layout, plot_layout, settings_layout):
        """
        Given a dataframe and a layout spec
        this class populates appropriate radio button functionality
        """
        self.df = df
        self.parent_layout = parent_layout
        self.settings_layout = settings_layout
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

    def get_radio_buttons(self):
        # Returns a dict of the radio buttons created
        return self.buttons

    def create_canvas(self):
        sc = MyStaticMplCanvas(self.parent_layout,
                               df=self.df,
                               width=5,
                               height=4,
                               dpi=100,
                               plot_type='histogram')

        self.plot_layout.addWidget(sc)
