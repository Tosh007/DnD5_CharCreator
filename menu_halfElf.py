# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_HalfElf.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_halfElf(object):
    def setupUi(self, singleCheckableCombobox):
        singleCheckableCombobox.setObjectName("singleCheckableCombobox")
        singleCheckableCombobox.setGeometry(QtCore.QRect(0, 0, 261, 151))
        self.comboBox1 = CheckableComboBox(singleCheckableCombobox)
        self.comboBox1.setGeometry(QtCore.QRect(30, 60, 161, 22))
        self.comboBox1.setObjectName("comboBox1")
        self.label = QtWidgets.QLabel(singleCheckableCombobox)
        self.label.setGeometry(QtCore.QRect(30, 30, 131, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(singleCheckableCombobox)
        self.comboBox.setGeometry(QtCore.QRect(30, 27, 161, 21))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(singleCheckableCombobox)
        QtCore.QMetaObject.connectSlotsByName(singleCheckableCombobox)

    def retranslateUi(self, singleCheckableCombobox):
        _translate = QtCore.QCoreApplication.translate
        singleCheckableCombobox.setWindowTitle(_translate("halfElf", "Form"))

from checkableCombobox import CheckableComboBox
