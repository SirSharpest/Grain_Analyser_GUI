# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataview.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DataWindow(object):
    def setupUi(self, DataWindow):
        DataWindow.setObjectName("DataWindow")
        DataWindow.resize(352, 315)
        self.centralwidget = QtWidgets.QWidget(DataWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tbl_data = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_data.setObjectName("tbl_data")
        self.tbl_data.setColumnCount(0)
        self.tbl_data.setRowCount(0)
        self.gridLayout.addWidget(self.tbl_data, 0, 0, 1, 1)
        DataWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DataWindow)
        QtCore.QMetaObject.connectSlotsByName(DataWindow)

    def retranslateUi(self, DataWindow):
        _translate = QtCore.QCoreApplication.translate
        DataWindow.setWindowTitle(_translate("DataWindow", "Data View"))

