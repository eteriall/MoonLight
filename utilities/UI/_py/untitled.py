# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(408, 538)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.load_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load_btn.setGeometry(QtCore.QRect(270, 10, 131, 81))
        self.load_btn.setObjectName("load_btn")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 241, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.speed_field = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.speed_field.setObjectName("speed_field")
        self.horizontalLayout.addWidget(self.speed_field)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.distance_field = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.distance_field.setObjectName("distance_field")
        self.horizontalLayout_2.addWidget(self.distance_field)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.vd_field = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.vd_field.setObjectName("vd_field")
        self.horizontalLayout_3.addWidget(self.vd_field)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.od_field = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.od_field.setObjectName("od_field")
        self.horizontalLayout_4.addWidget(self.od_field)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(160, 410, 241, 101))
        self.start_btn.setObjectName("start_btn")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(20, 410, 141, 101))
        self.stop_btn.setObjectName("stop_btn")
        self.save_vtn = QtWidgets.QPushButton(self.centralwidget)
        self.save_vtn.setGeometry(QtCore.QRect(270, 90, 131, 81))
        self.save_vtn.setObjectName("save_vtn")
        self.table = QtWidgets.QTableView(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(20, 170, 371, 231))
        self.table.setObjectName("table")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Moon Light Software"))
        self.load_btn.setText(_translate("MainWindow", "??????????????????"))
        self.label.setText(_translate("MainWindow", "???????????????? ??????????????"))
        self.label_2.setText(_translate("MainWindow", "????????????????????"))
        self.label_3.setText(_translate("MainWindow", "D ??????????????"))
        self.label_4.setText(_translate("MainWindow", "D ???????????????? "))
        self.start_btn.setText(_translate("MainWindow", "??????????"))
        self.stop_btn.setText(_translate("MainWindow", "????????"))
        self.save_vtn.setText(_translate("MainWindow", "??????????????????"))
