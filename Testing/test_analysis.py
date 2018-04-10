import sys
import pytest
sys.path.append("./model/")
sys.path.append("./controller/")
sys.path.append("./view/")
from test_GUI import app_and_window, DATA_FOLDER, EXTRA_INFO, take_screenshot
from PyQt5.QtWidgets import QApplication
from gui_controller import AppWindow
from PyQt5.QtCore import Qt
from time import sleep


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
    aw[1].ui.expinfo.setText(EXTRA_INFO)
    aw[1].pre_process_controller.load_experimental_data()
    aw[1].pre_process_controller.clean_data()
    aw[1].ui.master_tab.setCurrentIndex(2)
    yield aw
    aw[0].quit()


def test_analysis_window_loads(setup_data, qtbot):
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_analysis_window_loads.png', setup_data[1])


def test_analysis_window_hist_rb_1(setup_data, qtbot):
    setup_data[1].analysis_controller.view.get_radio_buttons()[
        'volume'].setChecked(True)
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_analysis_window_hist_rb_1.png',
                    setup_data[1])


def test_analysis_window_hist_rb_2(setup_data, qtbot):
    setup_data[1].analysis_controller.view.get_radio_buttons()[
        'width'].setChecked(True)
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_analysis_window_hist_rb_2.png', setup_data[1])


def test_analysis_window_hist_groupby_1_rb_1(setup_data, qtbot):
    setup_data[1].analysis_controller.view.get_cb_group_by().setCurrentIndex(1)
    setup_data[1].analysis_controller.view.get_radio_buttons()[
        'volume'].setChecked(True)
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_analysis_window_hist_groupby_1_rb_1.png',
                    setup_data[1])


def test_analysis_window_hist_groupby_1_rb_2(setup_data, qtbot):
    setup_data[1].analysis_controller.view.get_cb_group_by().setCurrentIndex(2)
    setup_data[1].analysis_controller.view.get_radio_buttons()[
        'width'].setChecked(True)
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot(
        'test_analysis_window_hist_groupby_1_rb_2.png', setup_data[1])


def test_analysis_window_box_rb_1(setup_data, qtbot):
    setup_data[1].ui.cb_graph_type.setCurrentIndex(1)
    setup_data[1].analysis_controller.view.get_radio_buttons()[
        'width'].setChecked(True)
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_analysis_window_box_rb_1.png', setup_data[1])


def test_analysis_window_box_rb_2(setup_data, qtbot):
    setup_data[1].ui.cb_graph_type.setCurrentIndex(1)
    setup_data[1].analysis_controller.view.get_radio_buttons()[
        'width'].setChecked(True)
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_analysis_window_box_rb_2.png', setup_data[1])


def test_analysis_window_box_groupby_1_rb_1(setup_data, qtbot):
    setup_data[1].ui.cb_graph_type.setCurrentIndex(1)
    setup_data[1].analysis_controller.view.get_cb_group_by().setCurrentIndex(1)
    setup_data[1].analysis_controller.view.get_radio_buttons()[
        'width'].setChecked(True)
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot(
        'test_analysis_window_box_groupby_1_rb_1.png', setup_data[1])


def test_analysis_window_box_groupby_2_rb_2(setup_data, qtbot):
    setup_data[1].ui.cb_graph_type.setCurrentIndex(1)
    setup_data[1].analysis_controller.view.get_cb_group_by().setCurrentIndex(2)
    setup_data[1].analysis_controller.view.get_radio_buttons()[
        'width'].setChecked(True)
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot(
        'test_analysis_window_box_groupby_2_rb_2.png', setup_data[1])
