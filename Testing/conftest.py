import pytest
import sys
sys.path.append("./model/")
sys.path.append("./controller/")
sys.path.append("./view/")
from gui_controller import AppWindow
from PyQt5.QtWidgets import QApplication

DATA_FOLDER = 'Testing/Test_Data/'
EXTRA_INFO = 'Testing/Test_Files/extra_information.xlsx'


def pytest_sessionstart(session):
    """ before session.main() is called. """
    for i in range(0, 2):
        app = QApplication(sys.argv)
        w = AppWindow()
        w.showMaximized()
        aw = (app, w)
        aw[1].ui.directory.setText(DATA_FOLDER)
        aw[1].ui.rdb_rachis_yes.setChecked(False)
        aw[1].ui.btn_load_data.click()
        aw[1].ui.master_tab.setCurrentIndex(1)
        aw[1].ui.expinfo.setText(EXTRA_INFO)
        aw[1].pre_process_controller.load_experimental_data()
        aw[1].pre_process_controller.clean_data()
        aw[1].ui.master_tab.setCurrentIndex(2)
        aw
        aw[0].quit()
