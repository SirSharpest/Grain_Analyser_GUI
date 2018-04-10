from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui
from analysis_controller import AnalysisWindow
from load_data_controller import FindFilesWindow
from pre_processing_controller import PreProcessWindow
from stats_test_controller import StatsTestWindow
from main_view import Ui_MainWindow
from data_view import Ui_DataWindow
from pandas_model import PandasModel


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
        self.setup_menu_functions()

        # Load in Controllers
        self.find_files_controller = FindFilesWindow(self, self.ui)
        self.analysis_controller = AnalysisWindow(self, self.ui)
        self.ui.master_tab.currentChanged.connect(self.update_analysis_view)
        self.pre_process_controller = PreProcessWindow(self, self.ui)
        self.stats_test_controller = StatsTestWindow(self, self.ui)

        # Set GUI icon for beautification
        self.setWindowIcon(QtGui.QIcon('./images/logo.png'))

        # init some variables
        # Words cannot describe the importance of this object
        self.data = None

        # init states
        self.setup_default_states()
        self.show()

    def setup_menu_functions(self):
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionView_Data_Frame.triggered.connect(self.view_data)

    def setup_default_states(self):
        # Set the other tabs to disabled when no data is loaded
        self.ui.tab_preprocess.setEnabled(False)
        self.ui.tab_analysis.setEnabled(False)
        self.ui.tab_testing.setEnabled(False)

    def view_data(self):
        self.data_view = DataWindow(self.data.get_data())
        self.data_view.show()

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def update_analysis_view(self, tab):
        if tab is 2:
            self.analysis_controller.update_view()
        elif tab is 3:
            self.stats_test_controller.update_view(self.data)
