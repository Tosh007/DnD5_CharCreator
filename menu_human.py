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
        Human.resize(261, 151)
        self.comboBox_abilityScore = CheckableComboBox(Human)
        self.comboBox_abilityScore.setGeometry(QtCore.QRect(20, 120, 121, 22))
        self.comboBox_abilityScore.setObjectName("comboBox_abilityScore")
        self.checkBox_variantTraits = QtWidgets.QCheckBox(Human)
        self.checkBox_variantTraits.setGeometry(QtCore.QRect(20, 10, 91, 17))
        self.checkBox_variantTraits.setObjectName("checkBox_variantTraits")
        self.comboBox_skill = QtWidgets.QComboBox(Human)
        self.comboBox_skill.setGeometry(QtCore.QRect(20, 40, 121, 22))
        self.comboBox_skill.setObjectName("comboBox_skill")
        self.comboBox_feat = QtWidgets.QComboBox(Human)
        self.comboBox_feat.setGeometry(QtCore.QRect(20, 80, 121, 22))
        self.comboBox_feat.setObjectName("comboBox_feat")
        self.label = QtWidgets.QLabel(Human)
        self.label.setGeometry(QtCore.QRect(150, 40, 17, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Human)
        self.label_2.setGeometry(QtCore.QRect(150, 80, 20, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Human)
        self.label_3.setGeometry(QtCore.QRect(150, 120, 91, 20))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Human)
        QtCore.QMetaObject.connectSlotsByName(Human)

    def retranslateUi(self, Human):
        _translate = QtCore.QCoreApplication.translate
        Human.setWindowTitle(_translate("Human", "Form"))
        self.checkBox_variantTraits.setText(_translate("Human", "Variant Traits"))
        self.label.setText(_translate("Human", "Skill"))
        self.label_2.setText(_translate("Human", "feat"))
        self.label_3.setText(_translate("Human", "Ability Scores +1"))

from checkableCombobox import CheckableComboBox
