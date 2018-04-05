import sys
import pytest
sys.path.append("./model/")
sys.path.append("./controller/")
sys.path.append("./view/")
from gui_controller import AppWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from PyQt5 import QtTest
import time
from pytestqt import qtbot


def test_startup(qtbot):
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    QtTest.QTest.mouseClick(w.ui.btn_find_files, QtCore.Qt.LeftButton)
    time.sleep(5)
