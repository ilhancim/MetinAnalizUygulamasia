# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(281, 482)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pb1 = QtWidgets.QPushButton(self.centralwidget)
        self.pb1.setGeometry(QtCore.QRect(10, 10, 261, 71))
        self.pb1.setObjectName("pb1")
        self.pb2 = QtWidgets.QPushButton(self.centralwidget)
        self.pb2.setGeometry(QtCore.QRect(10, 95, 261, 71))
        self.pb2.setObjectName("pb2")
        self.pb3 = QtWidgets.QPushButton(self.centralwidget)
        self.pb3.setGeometry(QtCore.QRect(10, 180, 261, 71))
        self.pb3.setObjectName("pb3")
        self.pb4 = QtWidgets.QPushButton(self.centralwidget)
        self.pb4.setGeometry(QtCore.QRect(10, 265, 261, 71))
        self.pb4.setObjectName("pb4")
        self.pb5 = QtWidgets.QPushButton(self.centralwidget)
        self.pb5.setGeometry(QtCore.QRect(10, 350, 261, 71))
        self.pb5.setObjectName("pb5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 281, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Uygulama"))
        self.pb1.setText(_translate("MainWindow", "Metin Verilerini İşleme"))
        self.pb2.setText(_translate("MainWindow", "İstatistik"))
        self.pb3.setText(_translate("MainWindow", "Benzerlik Analizi"))
        self.pb4.setText(_translate("MainWindow", "Arama ve Filtreleme"))
        self.pb5.setText(_translate("MainWindow", "Veri depolama ve yönetim"))
