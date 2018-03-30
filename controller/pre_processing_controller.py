from PyQt5.QtWidgets import QFileDialog, QMessageBox
from ct_analysing_library.ct_data import NoDataFoundException


class PreProcessWindow():
    def __init__(self, window, ui):
        self.window = window
        self.ui = ui
        self.connect_view_functions()

    def connect_view_functions(self):
        self.ui.btn_select_expinfo.clicked.connect(
            self.select_experimental_info)

        # TODO Fix naming conventions in the UI forms
        self.ui.btn_loadexpinfo.clicked.connect(self.load_experimental_data)

    def select_experimental_info(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        info, _ = QFileDialog.getOpenFileName(
            self.window, "QFileDialog.getOpenFileName()", "", "Excel Files (*.xlsx)", options=options)
        self.ui.expinfo.setText(info)

    def load_experimental_data(self):
        try:
            finfo = self.ui.expinfo.text()
            self.window.get_data().get_spike_info(finfo)
        except (ValueError, NoDataFoundException):
            QMessageBox.warning(self.window, "Whoops",
                                "That data is not matching with loaded data")
