# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName("Wizard")
        Wizard.resize(261, 181)
        self.gridLayout = QtWidgets.QGridLayout(Wizard)
        self.gridLayout.setObjectName("gridLayout")
        self.label_numPreparedSpells = QtWidgets.QLabel(Wizard)
        self.label_numPreparedSpells.setObjectName("label_numPreparedSpells")
        self.gridLayout.addWidget(self.label_numPreparedSpells, 0, 0, 1, 1)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        _translate = QtCore.QCoreApplication.translate
        Wizard.setWindowTitle(_translate("Wizard", "Form"))
        self.label_numPreparedSpells.setText(_translate("Wizard", "<Spells to prepare> "))

