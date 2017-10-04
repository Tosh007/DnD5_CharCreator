# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_twoCombobox.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_twoCombobox(object):
    def setupUi(self, twoCombobox):
        twoCombobox.setObjectName("twoCombobox")
        twoCombobox.resize(261, 151)
        self.comboBox1 = QtWidgets.QComboBox(twoCombobox)
        self.comboBox1.setGeometry(QtCore.QRect(30, 60, 161, 22))
        self.comboBox1.setObjectName("comboBox1")
        self.label = QtWidgets.QLabel(twoCombobox)
        self.label.setGeometry(QtCore.QRect(30, 30, 131, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.comboBox2 = QtWidgets.QComboBox(twoCombobox)
        self.comboBox2.setGeometry(QtCore.QRect(30, 100, 161, 22))
        self.comboBox2.setObjectName("comboBox2")

        self.retranslateUi(twoCombobox)
        QtCore.QMetaObject.connectSlotsByName(twoCombobox)

    def retranslateUi(self, twoCombobox):
        _translate = QtCore.QCoreApplication.translate
        twoCombobox.setWindowTitle(_translate("twoCombobox", "Form"))

