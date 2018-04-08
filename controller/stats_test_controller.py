from PyQt5.QtWidgets import QFileDialog, QMessageBox
from matplotlib_canvas_model import MyStaticMplCanvas
from matplotlib_canvas_view import TestWindowView as view


class StatsTestWindow():
    def __init__(self, window, ui):
        self.window = window
        self.ui = ui
        self.connect_view_functions()
        self.plot_type = "boxplot"

    def connect_view_functions(self):
        self.ui.cb_test_grouping.currentTextChanged.connect(self.set_group_by)
        self.ui.rbtn_bayes.toggled.connect(self.set_test_type)
        self.ui.rbtn_ttest.toggled.connect(self.set_test_type)
        self.ui.btn_test.clicked.connect(self.setup_figure_canvas)

    def set_test_type(self):
        pass

    def set_group_by(self):
        # When grouping is changed then we need to update options
        self.ui.cb_test_g1.clear()
        self.ui.cb_test_g2.clear()
        groups = list(self.window.get_data().get_data()[
                      self.ui.cb_test_grouping.currentText()].unique())
        self.ui.cb_test_g1.addItems(groups)
        self.ui.cb_test_g2.addItems(groups)

    def refresh(self, data):
        self.view = view(
            self.window.get_data().get_data(),
            self.ui,
            self.plot_type)

    def update_view(self, data):
        """
        Attach this function to tab onclick
        then when the data changes we can create a new view
        with any changes to the columns!
        """
        self.refresh(data)

    def setup_figure_canvas(self):
        self.make_canvas_plot(self.plot_type)

    def get_group_by(self):
        return self.view.get_cb_group_by().currentText()

    def make_canvas_plot(self, plot_type):
        # delete old plot
        for i in reversed(range(self.ui.layout_test_plots.count())):
            self.ui.layout_test_plots.itemAt(i).widget().deleteLater()

        column = self.ui.cb_test_attribute.currentText()
        for i in reversed(range(self.ui.layout_plots.count())):
            self.ui.layout_plots.itemAt(i).widget().deleteLater()
        self.sc = MyStaticMplCanvas(self.ui.tab_testing,
                                    self.window,
                                    self.window.get_data().get_data(),  # This will need altered
                                    width=5,
                                    height=4,
                                    dpi=100,
                                    column=column,
                                    plot_type=self.plot_type,
                                    group_by=self.ui.cb_test_grouping.currentText())
        self.ui.layout_test_plots.addWidget(self.sc)
