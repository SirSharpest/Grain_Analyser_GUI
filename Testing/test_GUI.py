import sys
import inspect
import pytest
sys.path.append("./model/")
sys.path.append("./controller/")
sys.path.append("./view/")
from gui_controller import AppWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from PyQt5 import QtTest
import time


DATA_FOLDER = 'Testing/Test_Data/'
EXTRA_INFO = 'Testing/Test_Files/extra_information.xlsx'


@pytest.fixture
def app_and_window():
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    return (app, w)


def take_screenshot(fname, window):
    p = window.grab()
    p.save('./Testing/Screenshots/{0}'.format(fname))


def test_startup(app_and_window):
    app_and_window[0].quit()
