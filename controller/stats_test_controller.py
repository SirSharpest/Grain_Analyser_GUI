from PyQt5.QtWidgets import QFileDialog, QMessageBox
from matplotlib_canvas_model import MyStaticMplCanvas
from matplotlib_canvas_view import TestWindowView as view


class StatsTestWindow():
    def __init__(self, window, ui):
        self.window = window
        self.ui = ui
        self.connect_view_functions()
        self.plot_type = "boxplot"
        self.ui.rbtn_ttest.setChecked(True)

    def connect_view_functions(self):
        self.ui.cb_test_grouping.currentTextChanged.connect(self.set_group_by)
        self.ui.rbtn_bayes.toggled.connect(self.set_test_type)
        self.ui.rbtn_ttest.toggled.connect(self.set_test_type)
        self.ui.btn_test.clicked.connect(self.setup_figure_canvas)

    def set_test_type(self):
        self.plot_type = "boxplot" if self.ui.rbtn_ttest.isChecked() else "bayes"

    def set_group_by(self):
        # When grouping is changed then we need to update options
        self.ui.cb_test_g1.clear()
        self.ui.cb_test_g2.clear()
        groups = list(self.window.get_data().get_data()[
                      self.ui.cb_test_grouping.currentText()].unique())
        self.ui.cb_test_g1.addItems(groups)
        self.ui.cb_test_g2.addItems(groups)

    def update_view(self):
        """
        Attach this function to tab onclick
        then when the data changes we can create a new view
        with any changes to the columns!
        """
        self.view = view(
            self.window.get_data().get_data(),
            self.ui,
            self.plot_type)
        self.make_canvas_plot(self.plot_type)

    def setup_figure_canvas(self):
        if self.ui.cb_test_g1.currentText() == self.ui.cb_test_g2.currentText():
            self.ui.lbl_status.setText(
                'Warning identical data to be compared!')
        self.make_canvas_plot(self.plot_type)

    def get_group_by(self):
        return self.ui.cb_test_grouping.currentText()

    def slice_data(self):
        data = self.window.get_data().get_data()[(
            self.window.get_data().get_data()[self.get_group_by()]
            == self.ui.cb_test_g1.currentText()) | (
            self.window.get_data().get_data()[self.get_group_by()]
                == self.ui.cb_test_g2.currentText())]
        return data

    def make_canvas_plot(self, plot_type):
        # delete old plot
        for i in reversed(range(self.ui.layout_test_plots.count())):
            self.ui.layout_test_plots.itemAt(i).widget().setParent(None)
        column = self.ui.cb_test_attribute.currentText()

        self.sc = MyStaticMplCanvas(self.ui.tab_testing,
                                    self.window,
                                    self.slice_data(),
                                    width=5,
                                    height=4,
                                    dpi=100,
                                    column=column,
                                    plot_type=self.plot_type,
                                    group_by=self.ui.cb_test_grouping.currentText(),
                                    ttest=True)
        self.ui.layout_test_plots.addWidget(self.sc)
