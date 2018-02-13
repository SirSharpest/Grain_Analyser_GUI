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
        self.show()

    def setup_view_functions(self):
        # Load data page
        self.ui.btn_find_files.clicked.connect(self.search_for_files)
        self.ui.btn_to_csv.clicked.connect(self.grab_files)

    def grab_files(self):
        try:
            self.data = data(self.ui.directory.text(),
                             self.ui.rdb_rachis_yes.isChecked())
        except:
            QMessageBox.warning(self, "Finding Files Error",
                                "Couldn't find files in given location")

    def search_for_files(self):
        self.folder = str(QFileDialog.getExistingDirectory(
            self, "Select Directory"))
        self.ui.directory.setText(self.folder)
