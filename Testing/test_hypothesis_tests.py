import sys
import pytest
sys.path.append("./model/")
sys.path.append("./controller/")
sys.path.append("./view/")
from test_GUI import app_and_window, DATA_FOLDER, EXTRA_INFO, take_screenshot
from PyQt5.QtWidgets import QApplication
from gui_controller import AppWindow
from PyQt5.QtCore import Qt


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
    aw[1].ui.master_tab.setCurrentIndex(3)
    yield aw
    aw[0].quit()


def test_hypothesis_window_loads(setup_data, qtbot):
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_hypothesis_window_loads.png', setup_data[1])


def test_hypothesis_ttest_g1_att_1(setup_data, qtbot):
    setup_data[1].ui.cb_test_attribute.setCurrentIndex(3)
    setup_data[1].ui.cb_test_grouping.setCurrentIndex(1)
    setup_data[1].ui.cb_test_g1.setCurrentIndex(1)
    setup_data[1].ui.cb_test_g2.setCurrentIndex(2)
    setup_data[1].ui.btn_test.click()
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_hypothesis_ttest_g1_att_1.png', setup_data[1])


def test_hypothesis_ttest_g2_att_1(setup_data, qtbot):
    setup_data[1].ui.cb_test_attribute.setCurrentIndex(3)
    setup_data[1].ui.cb_test_grouping.setCurrentIndex(2)
    setup_data[1].ui.cb_test_g1.setCurrentIndex(0)
    setup_data[1].ui.cb_test_g2.setCurrentIndex(0)
    setup_data[1].ui.btn_test.click()
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_hypothesis_ttest_g2_att_1.png', setup_data[1])


def test_hypothesis_ttest_g1_att_2(setup_data, qtbot):
    setup_data[1].ui.cb_test_attribute.setCurrentIndex(5)
    setup_data[1].ui.cb_test_grouping.setCurrentIndex(1)
    setup_data[1].ui.cb_test_g1.setCurrentIndex(1)
    setup_data[1].ui.cb_test_g2.setCurrentIndex(2)
    setup_data[1].ui.btn_test.click()
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_hypothesis_ttest_g1_att_2.png', setup_data[1])


def test_hypothesis_ttest_g2_att_2(setup_data, qtbot):
    setup_data[1].ui.cb_test_attribute.setCurrentIndex(5)
    setup_data[1].ui.cb_test_grouping.setCurrentIndex(2)
    setup_data[1].ui.cb_test_g1.setCurrentIndex(0)
    setup_data[1].ui.cb_test_g2.setCurrentIndex(0)
    setup_data[1].ui.btn_test.click()
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_hypothesis_ttest_g2_att_2.png', setup_data[1])


def test_hypothesis_bayestest_g1_att_1(setup_data, qtbot):
    setup_data[1].ui.cb_test_attribute.setCurrentIndex(3)
    setup_data[1].ui.rbtn_bayes.setChecked(True)
    setup_data[1].ui.cb_test_grouping.setCurrentIndex(1)
    setup_data[1].ui.cb_test_g1.setCurrentIndex(1)
    setup_data[1].ui.cb_test_g2.setCurrentIndex(2)
    setup_data[1].ui.btn_test.click()
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_hypothesis_bayestest_g1_att_1.png', setup_data[1])


def test_hypothesis_bayestest_g2_att_1(setup_data, qtbot):
    setup_data[1].ui.cb_test_attribute.setCurrentIndex(3)
    setup_data[1].ui.rbtn_bayes.setChecked(True)
    setup_data[1].ui.cb_test_grouping.setCurrentIndex(2)
    setup_data[1].ui.cb_test_g1.setCurrentIndex(0)
    setup_data[1].ui.cb_test_g2.setCurrentIndex(0)
    setup_data[1].ui.btn_test.click()
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_hypothesis_bayestest_g2_att_1.png', setup_data[1])


def test_hypothesis_bayestest_g1_att_2(setup_data, qtbot):
    setup_data[1].ui.cb_test_attribute.setCurrentIndex(5)
    setup_data[1].ui.rbtn_bayes.setChecked(True)
    setup_data[1].ui.cb_test_grouping.setCurrentIndex(1)
    setup_data[1].ui.cb_test_g1.setCurrentIndex(1)
    setup_data[1].ui.cb_test_g2.setCurrentIndex(2)
    setup_data[1].ui.btn_test.click()
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_hypothesis_bayestest_g1_att_2.png', setup_data[1])


def test_hypothesis_bayestest_g2_att_2(setup_data, qtbot):
    setup_data[1].ui.cb_test_attribute.setCurrentIndex(5)
    setup_data[1].ui.rbtn_bayes.setChecked(True)
    setup_data[1].ui.cb_test_grouping.setCurrentIndex(2)
    setup_data[1].ui.cb_test_g1.setCurrentIndex(0)
    setup_data[1].ui.cb_test_g2.setCurrentIndex(0)
    setup_data[1].ui.btn_test.click()
    qtbot.waitForWindowShown(setup_data[1])
    take_screenshot('test_hypothesis_bayestest_g2_att_2.png', setup_data[1])
