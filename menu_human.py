# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_human.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Human(object):
    def setupUi(self, Human):
        Human.setObjectName("Human")
        Human.resize(261, 181)
        self.comboBox_abilityScore1 = QtWidgets.QComboBox(Human)
        self.comboBox_abilityScore1.setGeometry(QtCore.QRect(20, 60, 81, 22))
        self.comboBox_abilityScore1.setObjectName("comboBox_abilityScore1")
        self.checkBox_variantTraits = QtWidgets.QCheckBox(Human)
        self.checkBox_variantTraits.setGeometry(QtCore.QRect(20, 20, 81, 17))
        self.checkBox_variantTraits.setObjectName("checkBox_variantTraits")
        self.comboBox_abilityScore2 = QtWidgets.QComboBox(Human)
        self.comboBox_abilityScore2.setGeometry(QtCore.QRect(20, 100, 81, 22))
        self.comboBox_abilityScore2.setObjectName("comboBox_abilityScore2")
        self.comboBox_skill = QtWidgets.QComboBox(Human)
        self.comboBox_skill.setGeometry(QtCore.QRect(120, 60, 121, 22))
        self.comboBox_skill.setObjectName("comboBox_skill")
        self.comboBox_feat = QtWidgets.QComboBox(Human)
        self.comboBox_feat.setGeometry(QtCore.QRect(120, 100, 121, 22))
        self.comboBox_feat.setObjectName("comboBox_feat")

        self.retranslateUi(Human)
        QtCore.QMetaObject.connectSlotsByName(Human)

    def retranslateUi(self, Human):
        _translate = QtCore.QCoreApplication.translate
        Human.setWindowTitle(_translate("Human", "Form"))
        self.checkBox_variantTraits.setText(_translate("Human", "Variant Traits"))

