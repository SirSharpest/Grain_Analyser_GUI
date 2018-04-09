from PyQt5.QtWidgets import QFileDialog, QMessageBox
from data_model import CTGUIData
from list_model import WidgetList


class DataAlreadyLoaded(Exception):
    pass


class FindFilesWindow():
    def __init__(self, window, ui):
        self.ui = ui
        self.window = window
        self.connect_view_functions()
        self.set_default_states()
        self.wdg_lst_files = None

    def connect_view_functions(self):
        # Load data page
        self.ui.btn_find_files.clicked.connect(self.search_for_files)
        self.ui.btn_load_data.clicked.connect(self.find_files)
        self.ui.btn_to_csv.clicked.connect(self.save_file_dialog)

    def set_default_states(self):
        # This should be off by default
        # until the user has loaded data
        self.ui.btn_to_csv.setEnabled(False)
        self.ui.rdb_rachis_yes.setChecked(True)

    def find_files(self):
        try:
            if self.window.get_data() is not None:
                raise DataAlreadyLoaded
            self.window.set_data(CTGUIData(self.ui.directory.text(),
                                           self.ui.rdb_rachis_yes.isChecked()))
            if self.window.get_data():
                self.ui.btn_to_csv.setEnabled(True)
                self.ui.tab_preprocess.setEnabled(True)
                self.ui.tab_analysis.setEnabled(True)
                self.set_files_list()
                self.ui.lbl_status.setText('Data loaded!')
        except TypeError as e:
            QMessageBox.warning(self.window, "Finding Files Error",
                                "Couldn't find files in given location")
        except DataAlreadyLoaded as e:
            QMessageBox.warning(self.window, "Data Already Loaded",
                                "Sorry! You've already loaded in data")

    def save_file_dialog(self):
        if self.window.get_data() is None:
            QMessageBox.warning(self.window,
                                "No data",
                                "Data hasn't been loaded")
            return
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            filename, _ = QFileDialog.getSaveFileName(
                self.window,
                "Save Files",
                "",
                "CSV Files (*.csv)",
                options=options)
            if filename:
                self.window.get_data().download_data(filename)
            else:
                QMessageBox.warning(self.window, "Invalid Location",
                                    "Couldn't find the save location")
        except TypeError as e:
            QMessageBox.warning(self.window, "Bad Parameters!",
                                "Invalid save options")

    def search_for_files(self):
        self.folder = str(QFileDialog.getExistingDirectory(
            self.window, "Select Directory"))
        self.ui.directory.setText(self.folder)

    def set_files_list(self):
        if self.wdg_lst_files is None:
            self.wdg_lst_files = WidgetList(self.ui.lst_files)
        g, r = self.window.get_data().get_files()
        self.wdg_lst_files.update(g)
