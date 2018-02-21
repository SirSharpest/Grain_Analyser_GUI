from matplotlib_canvas_model import MyStaticMplCanvas
from matplotlib_canvas_view import MatplotlibCanvasView as view


class AnalysisWindow():
    def __init__(self, ui):
        self.ui = ui
        self.data = None
        self.view = None

    def setup_default_states(self):
        pass

    def enable(self, data):
        self.update_data(data)
        self.view = view(
            self.data.get_data(),
            self.ui.tab_analysis,
            self.ui.layout_plots,
            self.ui.layout_plot_settings)
        self.setup_figure_canvas()

    def update_data(self, data):
        self.data = data

    def setup_figure_canvas(self):
        for k, v in self.view.get_radio_buttons().items():
            v.toggled.connect(self.make_canvas_plot)
        self.make_canvas_plot()

    def find_clicked_button(self):
        for k, v in self.view.get_radio_buttons().items():
            if v.isChecked():
                return v.column
        return 'volume'

    def make_canvas_plot(self):
        column = self.find_clicked_button()
        for i in reversed(range(self.ui.layout_plots.count())):
            self.ui.layout_plots.itemAt(i).widget().deleteLater()
        self.sc = MyStaticMplCanvas(self.ui.tab_analysis,
                                    self.data.get_data(),
                                    width=5,
                                    height=4,
                                    dpi=100,
                                    column=column,
                                    plot_type='histogram')
        self.ui.layout_plots.addWidget(self.sc)