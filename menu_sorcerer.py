# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_sorcerer.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Sorcerer(object):
    def setupUi(self, Sorcerer):
        Sorcerer.setObjectName("Sorcerer")
        Sorcerer.resize(261, 151)
        self.verticalLayout = QtWidgets.QVBoxLayout(Sorcerer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Sorcerer)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox1 = QtWidgets.QComboBox(Sorcerer)
        self.comboBox1.setObjectName("comboBox1")
        self.verticalLayout.addWidget(self.comboBox1)
        self.label_2 = QtWidgets.QLabel(Sorcerer)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(Sorcerer)
        QtCore.QMetaObject.connectSlotsByName(Sorcerer)

    def retranslateUi(self, Sorcerer):
        _translate = QtCore.QCoreApplication.translate
        Sorcerer.setWindowTitle(_translate("Sorcerer", "Form"))
        self.label_2.setText(_translate("Sorcerer", "You have two spell slots of level 1"))

