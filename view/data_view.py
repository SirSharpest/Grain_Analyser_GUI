# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataview.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wdg_dataview(object):
    def setupUi(self, wdg_dataview):
        wdg_dataview.setObjectName("wdg_dataview")
        wdg_dataview.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(wdg_dataview)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tbl_data = QtWidgets.QTableWidget(wdg_dataview)
        self.tbl_data.setObjectName("tbl_data")
        self.tbl_data.setColumnCount(0)
        self.tbl_data.setRowCount(0)
        self.gridLayout_2.addWidget(self.tbl_data, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(wdg_dataview)
        QtCore.QMetaObject.connectSlotsByName(wdg_dataview)

    def retranslateUi(self, wdg_dataview):
        _translate = QtCore.QCoreApplication.translate
        wdg_dataview.setWindowTitle(_translate("wdg_dataview", "Data  View"))

