from PyQt5.QtWidgets import QMainWindow,  QWidget, QPushButton, QAction, QFileDialog, QMessageBox, QMenu
from PyQt5 import QtGui
from main_view import Ui_MainWindow
from data_view import Ui_DataWindow
from matplotlib_canvas_view import MatplotlibCanvasView as analysis_view
from data_model import CTGUIData as data
from list_model import WidgetList
from pandas_model import PandasModel
from matplotlib_canvas_model import MyStaticMplCanvas
# May need to rearrange import order
import sys

"""
Issues: When self.data changes/updates then analysis_view will be outdated

"""


class DataWindow(QMainWindow):
    def __init__(self, df):
        super().__init__()
        self.ui = Ui_DataWindow()
        self.ui.setupUi(self)
        self.populate_table(df)

    def populate_table(self, df):
        self.model = PandasModel(self.ui.tbl_data, df)


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.analysis_view = None
        self.setup_menu_functions()
        self.setup_view_functions()
        self.setWindowIcon(QtGui.QIcon('./images/logo.png'))

        # init some variables
        self.data = None
        self.wdg_lst_files = None
        # init states
        self.setup_default_states()
        self.show()

    def setup_menu_functions(self):
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionView_Data_Frame.triggered.connect(self.view_data)
        self.ui.actionSave_Data.triggered.connect(self.save_file_dialog)

    def setup_default_states(self):
        # This should be off by default
        # until the user has loaded data
        self.ui.btn_to_csv.setEnabled(False)
        self.ui.rdb_rachis_yes.setChecked(True)

        # Set the other tabs to disabled when no data is loaded
        self.ui.tab_preprocess.setEnabled(False)
        self.ui.tab_analysis.setEnabled(False)

    def setup_view_functions(self):
        # Load data page
        self.ui.btn_find_files.clicked.connect(self.search_for_files)
        self.ui.btn_load_data.clicked.connect(self.find_files)
        self.ui.btn_to_csv.clicked.connect(self.save_file_dialog)

    def setup_figure_canvas(self):
        for k, v in self.analysis_view.get_radio_buttons().items():
            v.toggled.connect(self.make_canvas_plot)
        self.make_canvas_plot()

    def find_clicked_button(self):
        for k, v in self.analysis_view.get_radio_buttons().items():
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

    def view_data(self):
        self.data_view = DataWindow(self.data.get_data())
        self.data_view.show()

    def find_files(self):
        try:
            self.data = data(self.ui.directory.text(),
                             self.ui.rdb_rachis_yes.isChecked())
            if self.data:
                self.ui.btn_to_csv.setEnabled(True)
                self.ui.tab_preprocess.setEnabled(True)
                self.ui.tab_analysis.setEnabled(True)
                self.analysis_view = analysis_view(
                    self.data.get_data(),
                    self.ui.tab_analysis,
                    self.ui.layout_plots,
                    self.ui.layout_plot_settings)
                self.setup_figure_canvas()
                self.set_files_list()
        except TypeError as e:
            QMessageBox.warning(self, "Finding Files Error",
                                "Couldn't find files in given location")
            sys.stderr.write(e)

    def set_files_list(self):
        if self.wdg_lst_files is None:
            self.wdg_lst_files = WidgetList(self.ui.lst_files)
        g, r = self.data.get_files()
        self.wdg_lst_files.update(g)

    def save_file_dialog(self):
        if self.data is None:
            QMessageBox.warning(self, "No data", "Data hasn't been loaded")
            return
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            filename, _ = QFileDialog.getSaveFileName(
                self, "Save Files", "", "CSV Files (*.csv)", options=options)
            if filename:
                self.data.download_data(filename)
            else:
                QMessageBox.warning(self, "Invalid Location",
                                    "Couldn't find the save location")
        except TypeError as e:
            QMessageBox.warning(self, "Bad Parameters!",
                                "Invalid save options")
            sys.stderr.write(e)

    def search_for_files(self):
        self.folder = str(QFileDialog.getExistingDirectory(
            self, "Select Directory"))
        self.ui.directory.setText(self.folder)
