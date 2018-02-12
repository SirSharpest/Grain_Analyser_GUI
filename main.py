import sys
sys.path.append("./view/")
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction

# WARNING This name will change when it's refactored to be named correctly!
from main_view import Ui_MainWindow


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
