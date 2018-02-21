# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 566)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.master_tab = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.master_tab.sizePolicy().hasHeightForWidth())
        self.master_tab.setSizePolicy(sizePolicy)
        self.master_tab.setObjectName("master_tab")
        self.tab_load = QtWidgets.QWidget()
        self.tab_load.setObjectName("tab_load")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_load)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rdb_rachis_yes = QtWidgets.QRadioButton(self.tab_load)
        self.rdb_rachis_yes.setObjectName("rdb_rachis_yes")
        self.gridLayout_2.addWidget(self.rdb_rachis_yes, 1, 1, 1, 1)
        self.rdb_rachis_no = QtWidgets.QRadioButton(self.tab_load)
        self.rdb_rachis_no.setObjectName("rdb_rachis_no")
        self.gridLayout_2.addWidget(self.rdb_rachis_no, 2, 1, 1, 1)
        self.directory = QtWidgets.QLineEdit(self.tab_load)
        self.directory.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.directory.sizePolicy().hasHeightForWidth())
        self.directory.setSizePolicy(sizePolicy)
        self.directory.setObjectName("directory")
        self.gridLayout_2.addWidget(self.directory, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btn_to_csv = QtWidgets.QPushButton(self.tab_load)
        self.btn_to_csv.setObjectName("btn_to_csv")
        self.horizontalLayout_3.addWidget(self.btn_to_csv)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_load)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.btn_find_files = QtWidgets.QPushButton(self.tab_load)
        self.btn_find_files.setObjectName("btn_find_files")
        self.gridLayout_2.addWidget(self.btn_find_files, 0, 0, 1, 1)
        self.btn_load_data = QtWidgets.QPushButton(self.tab_load)
        self.btn_load_data.setObjectName("btn_load_data")
        self.gridLayout_2.addWidget(self.btn_load_data, 3, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.lst_files = QtWidgets.QListWidget(self.tab_load)
        self.lst_files.setObjectName("lst_files")
        self.verticalLayout_2.addWidget(self.lst_files)
        self.master_tab.addTab(self.tab_load, "")
        self.tab_preprocess = QtWidgets.QWidget()
        self.tab_preprocess.setObjectName("tab_preprocess")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_preprocess)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_loadexpinfo = QtWidgets.QPushButton(self.tab_preprocess)
        self.btn_loadexpinfo.setObjectName("btn_loadexpinfo")
        self.gridLayout_3.addWidget(self.btn_loadexpinfo, 1, 0, 1, 1)
        self.expinfo = QtWidgets.QLineEdit(self.tab_preprocess)
        self.expinfo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expinfo.sizePolicy().hasHeightForWidth())
        self.expinfo.setSizePolicy(sizePolicy)
        self.expinfo.setObjectName("expinfo")
        self.gridLayout_3.addWidget(self.expinfo, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chk_large = QtWidgets.QCheckBox(self.tab_preprocess)
        self.chk_large.setObjectName("chk_large")
        self.horizontalLayout.addWidget(self.chk_large)
        self.chk_small = QtWidgets.QCheckBox(self.tab_preprocess)
        self.chk_small.setObjectName("chk_small")
        self.horizontalLayout.addWidget(self.chk_small)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 3, 1, 1, 1)
        self.ctn_clean = QtWidgets.QPushButton(self.tab_preprocess)
        self.ctn_clean.setObjectName("ctn_clean")
        self.gridLayout_3.addWidget(self.ctn_clean, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.master_tab.addTab(self.tab_preprocess, "")
        self.tab_analysis = QtWidgets.QWidget()
        self.tab_analysis.setObjectName("tab_analysis")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_analysis)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.layout_plots = QtWidgets.QGridLayout()
        self.layout_plots.setObjectName("layout_plots")
        self.gridLayout_5.addLayout(self.layout_plots, 1, 0, 1, 1)
        self.layout_plot_settings = QtWidgets.QGridLayout()
        self.layout_plot_settings.setObjectName("layout_plot_settings")
        self.gridLayout_5.addLayout(self.layout_plot_settings, 0, 0, 1, 1)
        self.master_tab.addTab(self.tab_analysis, "")
        self.verticalLayout.addWidget(self.master_tab)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 722, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menuBar)
        self.actionView_Data_Frame = QtWidgets.QAction(MainWindow)
        self.actionView_Data_Frame.setObjectName("actionView_Data_Frame")
        self.actionSave_Data = QtWidgets.QAction(MainWindow)
        self.actionSave_Data.setObjectName("actionSave_Data")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionSave_Data)
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionView_Data_Frame)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.master_tab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CT-Seed Analyser 3000"))
        self.rdb_rachis_yes.setText(_translate("MainWindow", "&Yes"))
        self.rdb_rachis_no.setText(_translate("MainWindow", "&No"))
        self.btn_to_csv.setText(_translate("MainWindow", "Download to CSV"))
        self.label.setText(_translate("MainWindow", "Include Rachis data?"))
        self.btn_find_files.setText(_translate("MainWindow", "Find Files"))
        self.btn_load_data.setText(_translate("MainWindow", "Load Data"))
        self.lst_files.setSortingEnabled(False)
        self.master_tab.setTabText(self.master_tab.indexOf(self.tab_load), _translate("MainWindow", "Load Data"))
        self.btn_loadexpinfo.setText(_translate("MainWindow", "Load Experiment Info"))
        self.chk_large.setText(_translate("MainWindow", "Remove Large seeds"))
        self.chk_small.setText(_translate("MainWindow", "Remove Small Seeds"))
        self.ctn_clean.setText(_translate("MainWindow", "Clean Data"))
        self.master_tab.setTabText(self.master_tab.indexOf(self.tab_preprocess), _translate("MainWindow", "Pre-Processing"))
        self.master_tab.setTabText(self.master_tab.indexOf(self.tab_analysis), _translate("MainWindow", "Analysis"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionView_Data_Frame.setText(_translate("MainWindow", "&View Data Frame"))
        self.actionSave_Data.setText(_translate("MainWindow", "&Save Data"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))

