from PyQt5.QtWidgets import QFileDialog
from ct_analysing_library.ct_data import NoDataFoundException


class PreProcessWindow():
    def __init__(self, window, ui):
        self.window = window
        self.ui = ui
        self.connect_view_functions()

    def connect_view_functions(self):
        self.ui.btn_select_expinfo.clicked.connect(
            self.select_experimental_info)
        self.ui.btn_load_expinfo.clicked.connect(self.load_experimental_data)
        self.ui.btn_clean.clicked.connect(self.clean_data)

    def select_experimental_info(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        info, _ = QFileDialog.getOpenFileName(
            self.window,
            "QFileDialog.getOpenFileName()", "", "Excel Files (*.xlsx)",
            options=options)
        self.ui.expinfo.setText(info)

    def load_experimental_data(self):
        try:
            finfo = self.ui.expinfo.text()
            self.window.get_data().get_spike_info(finfo)
            # When extra data is loaded then we can do more with it!
            self.ui.tab_testing.setEnabled(True)
            self.ui.lbl_status.setText('Additional Data loaded!')
        except (ValueError, NoDataFoundException, FileNotFoundError):
            self.ui.lbl_status.setText('DATA NOT FOUND!')
            raise FileNotFoundError

    def clean_data(self):
        remove_large = self.ui.chk_large.isChecked()
        remove_small = self.ui.chk_small.isChecked()

        self.window.get_data().fix_colnames()
        self.window.get_data().clean_data(
            remove_small=remove_small, remove_large=remove_large)

        self.ui.lbl_status.setText(
            'Data cleaned! * Additional clicks will remove more data')
