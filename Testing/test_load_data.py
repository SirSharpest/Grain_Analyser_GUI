import sys
import pytest
sys.path.append("./model/")
sys.path.append("./controller/")
sys.path.append("./view/")
from test_GUI import app_and_window, DATA_FOLDER, take_screenshot


def test_load_data_without_rachis(app_and_window, qtbot):
    app_and_window[1].ui.directory.setText(DATA_FOLDER)
    app_and_window[1].ui.rdb_rachis_yes.setChecked(False)
    app_and_window[1].ui.btn_load_data.click()
    qtbot.waitForWindowShown(app_and_window[1])
    take_screenshot('test_load_data_without_rachis.png', app_and_window[1])
    app_and_window[0].quit()


def test_load_data_with_rachis(app_and_window, qtbot):
    app_and_window[1].ui.directory.setText(DATA_FOLDER)
    app_and_window[1].ui.rdb_rachis_yes.setChecked(True)
    app_and_window[1].ui.btn_load_data.click()
    qtbot.waitForWindowShown(app_and_window[1])
    take_screenshot('test_load_data_with_rachis.png', app_and_window[1])
    app_and_window[0].quit()
