#!/usr/bin/python3
"""
Main entry point for application

By Nathan Hughes
"""

import sys
sys.path.append("./model/")
sys.path.append("./controller/")
sys.path.append("./view/")
from gui_controller import AppWindow
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
