from PyQt5.QtWidgets import QMainWindow,  QWidget, QPushButton, QAction, QFileDialog, QMessageBox
from main_view import Ui_MainWindow
from data_model import CTGUIData as data


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_view_functions()

        # init some variables
        self.data = None

        # init states
        self.setup_default_states()
        self.show()

    def setup_default_states(self):
        # This should be off by default
        # until the user has loaded data
        self.ui.btn_to_csv.setEnabled(False)
        self.ui.rdb_rachis_yes.setChecked(True)

    def setup_view_functions(self):
        # Set default radio btn

        # Load data page
        self.ui.btn_find_files.clicked.connect(self.search_for_files)
        self.ui.btn_to_csv.clicked.connect(self.saveFileDialog)

    def grab_files(self):
        try:
            self.data = data(self.ui.directory.text(),
                             self.ui.rdb_rachis_yes.isChecked())
        except:
            QMessageBox.warning(self, "Finding Files Error",
                                "Couldn't find files in given location")

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(
            self, "QFileDialog.getSaveFileName()", "", "All Files (*);;CSV Files (*.csv)", options=options)
        if filename:
            self.data.download_data(filename)
        else:
            QMessageBox.warning(self, 'Couldn\'t find the save location')

    def search_for_files(self):
        self.folder = str(QFileDialog.getExistingDirectory(
            self, "Select Directory"))
        self.ui.directory.setText(self.folder)
        self.grab_files()
        if self.data:
            self.ui.btn_to_csv.setEnabled(True)
