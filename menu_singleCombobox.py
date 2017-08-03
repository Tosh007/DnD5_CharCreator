# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_singleCombobox.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_singleCombobox(object):
    def setupUi(self, singleCombobox):
        singleCombobox.setObjectName("singleCombobox")
        singleCombobox.resize(261, 151)
        self.comboBox1 = QtWidgets.QComboBox(singleCombobox)
        self.comboBox1.setGeometry(QtCore.QRect(30, 60, 161, 22))
        self.comboBox1.setObjectName("comboBox1")
        self.label = QtWidgets.QLabel(singleCombobox)
        self.label.setGeometry(QtCore.QRect(30, 30, 131, 16))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(singleCombobox)
        QtCore.QMetaObject.connectSlotsByName(singleCombobox)

    def retranslateUi(self, singleCombobox):
        _translate = QtCore.QCoreApplication.translate
        singleCombobox.setWindowTitle(_translate("singleCombobox", "Form"))

