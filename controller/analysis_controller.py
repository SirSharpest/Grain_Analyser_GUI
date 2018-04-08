from matplotlib_canvas_model import MyStaticMplCanvas
from matplotlib_canvas_view import AnalysisWindowView as view


class AnalysisWindow():
    def __init__(self, window, ui):
        self.ui = ui
        self.window = window
        self.view = None
        self.plot_type = 'histogram'
        self.ui.cb_graph_type.currentTextChanged.connect(self.set_graph_type)

    def set_graph_type(self):
        self.plot_type = str(self.ui.cb_graph_type.currentText()).lower()
        self.update_view(self.window.get_data())
        self.make_canvas_plot(self.plot_type)

    def refresh(self, data):
        print('creating view')
        self.view = view(
            self.window.get_data().get_data(),
            self.ui.tab_analysis,
            self.ui.layout_plots,
            self.ui.layout_plot_settings,
            self.plot_type)
        print('view created')
        self.setup_figure_canvas()

    def update_view(self, data):
        """
        Attach this function to tab onclick
        then when the data changes we can create a new view
        with any changes to the columns!
        """
        for i in reversed(range(self.ui.layout_plot_settings.count())):
            self.ui.layout_plot_settings.itemAt(i).widget().setParent(None)
        self.refresh(data)

    def setup_figure_canvas(self):
        for k, v in self.view.get_radio_buttons().items():
            v.toggled.connect(self.make_canvas_plot)
        self.make_canvas_plot(self.plot_type)

        self.view.get_cb_group_by().currentTextChanged.connect(self.make_canvas_plot)

    def find_clicked_button(self):
        for k, v in self.view.get_radio_buttons().items():
            if v.isChecked():
                return v.column
        return 'volume'

    def get_group_by(self):
        return self.view.get_cb_group_by().currentText()

    def make_canvas_plot(self, plot_type):
        column = self.find_clicked_button()
        for i in reversed(range(self.ui.layout_plots.count())):
            self.ui.layout_plots.itemAt(i).widget().deleteLater()
        self.sc = MyStaticMplCanvas(self.ui.tab_analysis,
                                    self.window,
                                    self.window.get_data().get_data(),
                                    width=5,
                                    height=4,
                                    dpi=100,
                                    column=column,
                                    plot_type=self.plot_type,
                                    group_by=self.get_group_by())
        self.ui.layout_plots.addWidget(self.sc)
