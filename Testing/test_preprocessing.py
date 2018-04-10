import sys
import pytest
sys.path.append("./model/")
sys.path.append("./controller/")
sys.path.append("./view/")
from test_GUI import app_and_window, DATA_FOLDER, EXTRA_INFO, take_screenshot
from PyQt5.QtWidgets import QApplication
from gui_controller import AppWindow


@pytest.fixture
def setup_data():
    app = QApplication(sys.argv)
    w = AppWindow()
    w.showMaximized()
    aw = (app, w)
    aw[1].ui.directory.setText(DATA_FOLDER)
    aw[1].ui.rdb_rachis_yes.setChecked(False)
    aw[1].ui.btn_load_data.click()
    aw[1].ui.master_tab.setCurrentIndex(1)
    yield aw
    aw[0].quit()


def test_load_additional_data(setup_data, qtbot):
    setup_data[1].ui.expinfo.setText(EXTRA_INFO)
    setup_data[1].pre_process_controller.load_experimental_data()
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_load_additional_data.png', setup_data[1])


def test_load_additional_data_expected_fail(setup_data, qtbot):
    setup_data[1].ui.expinfo.setText('folder/nofileshere/excel.xlsx')
    with pytest.raises(FileNotFoundError):
        setup_data[1].pre_process_controller.load_experimental_data()
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot(
        'test_load_additional_data_expected_fail.png', setup_data[1])


def test_clean_data_remove_none(setup_data, qtbot):
    setup_data[1].ui.expinfo.setText(EXTRA_INFO)
    setup_data[1].pre_process_controller.load_experimental_data()
    setup_data[1].pre_process_controller.clean_data()
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_clean_data_remove_none.png', setup_data[1])


def test_clean_data_remove_small(setup_data, qtbot):
    setup_data[1].ui.expinfo.setText(EXTRA_INFO)
    setup_data[1].pre_process_controller.load_experimental_data()
    setup_data[1].pre_process_controller.ui.chk_small.setChecked(True)
    setup_data[1].pre_process_controller.clean_data()
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_clean_data_remove_small.png', setup_data[1])


def test_clean_data_remove_large(setup_data, qtbot):
    setup_data[1].ui.expinfo.setText(EXTRA_INFO)
    setup_data[1].pre_process_controller.load_experimental_data()
    setup_data[1].pre_process_controller.ui.chk_large.setChecked(True)
    setup_data[1].pre_process_controller.clean_data()
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_clean_data_remove_large.png', setup_data[1])


def test_clean_data_remove_small_and_large(setup_data, qtbot):
    setup_data[1].ui.expinfo.setText(EXTRA_INFO)
    setup_data[1].pre_process_controller.load_experimental_data()
    setup_data[1].pre_process_controller.ui.chk_large.setChecked(True)
    setup_data[1].pre_process_controller.ui.chk_small.setChecked(True)
    setup_data[1].pre_process_controller.clean_data()
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot(
        'test_clean_data_remove_small_and_large.png', setup_data[1])
