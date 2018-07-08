# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_warlock.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Warlock(object):
    def setupUi(self, Warlock):
        Warlock.setObjectName("Warlock")
        Warlock.resize(261, 181)
        self.gridLayout = QtWidgets.QGridLayout(Warlock)
        self.gridLayout.setObjectName("gridLayout")
        self.label_spellSlotLevel = QtWidgets.QLabel(Warlock)
        self.label_spellSlotLevel.setObjectName("label_spellSlotLevel")
        self.gridLayout.addWidget(self.label_spellSlotLevel, 1, 0, 1, 1)
        self.label_spellSlots = QtWidgets.QLabel(Warlock)
        self.label_spellSlots.setObjectName("label_spellSlots")
        self.gridLayout.addWidget(self.label_spellSlots, 0, 0, 1, 1)

        self.retranslateUi(Warlock)
        QtCore.QMetaObject.connectSlotsByName(Warlock)

    def retranslateUi(self, Warlock):
        _translate = QtCore.QCoreApplication.translate
        Warlock.setWindowTitle(_translate("Warlock", "Form"))
        self.label_spellSlotLevel.setText(_translate("Warlock", "spell slot level"))
        self.label_spellSlots.setText(_translate("Warlock", "number of spell slots"))

