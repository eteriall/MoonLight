# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'experiment.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(555, 274)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setProperty("value", 0.8319)
        self.lcdNumber.setProperty("intValue", 1)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_3.addWidget(self.lcdNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setDigitCount(10)
        self.lcdNumber_2.setProperty("value", 12.45)
        self.lcdNumber_2.setProperty("intValue", 12)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout_2.addWidget(self.lcdNumber_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setDigitCount(10)
        self.lcdNumber_3.setProperty("value", 1.5)
        self.lcdNumber_3.setProperty("intValue", 2)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.horizontalLayout.addWidget(self.lcdNumber_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setMinimumSize(QtCore.QSize(0, 80))
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout_4.addWidget(self.stop_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Эксперимент #N, \"КОНФИГУРАЦИЯ\""))
        self.label.setText(_translate("MainWindow", "Время, (с)"))
        self.label_2.setText(_translate("MainWindow", "Дистанция, (мм)"))
        self.label_3.setText(_translate("MainWindow", "Нагрузка, (Н)"))
        self.pushButton.setText(_translate("MainWindow", "СТАРТ"))
        self.stop_btn.setText(_translate("MainWindow", "СТОП"))
