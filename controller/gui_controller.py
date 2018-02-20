from PyQt5.QtWidgets import QMainWindow,  QWidget, QPushButton, QAction, QFileDialog, QMessageBox, QMenu
from PyQt5 import QtGui
from main_view import Ui_MainWindow
from data_view import Ui_DataWindow
from data_model import CTGUIData as data
from list_model import WidgetList
from pandas_model import PandasModel
import sys

# this is a tmp import I think
import pandas as pd


class DataWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DataWindow()
        self.ui.setupUi(self)
        self.populate_table()

    def populate_table(self):
        # TODO Replace with actual code
        df = pd.read_csv('/home/nathan/primdata.csv')
        # Add sorting properly
        df = df.sort_values(by=['volume'])
        model = PandasModel(df)
        self.ui.tbl_data.setModel(model)


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
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

    def setup_view_functions(self):
        # Load data page
        self.ui.btn_find_files.clicked.connect(self.search_for_files)
        self.ui.btn_load_data.clicked.connect(self.find_files)
        self.ui.btn_to_csv.clicked.connect(self.save_file_dialog)

    def view_data(self):
        self.data_view = DataWindow()
        self.data_view.show()

    def find_files(self):
        try:
            self.data = data(self.ui.directory.text(),
                             self.ui.rdb_rachis_yes.isChecked())
            if self.data:
                self.ui.btn_to_csv.setEnabled(True)
                self.set_files_list()
        except TypeError as e:
            QMessageBox.warning(self, "Finding Files Error",
                                "Couldn't find files in given location")
            sys.stderr(e)

    def set_files_list(self):
        if self.wdg_lst_files:
            self.wdg_lst_files = WidgetList(self.ui.lst_files)
        g, r = self.data.get_files()
        self.wdg_lst_files.update(g)

    def save_file_dialog(self):
        if self.data:
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
            sys.stderr(e)

    def search_for_files(self):
        self.folder = str(QFileDialog.getExistingDirectory(
            self, "Select Directory"))
        self.ui.directory.setText(self.folder)
