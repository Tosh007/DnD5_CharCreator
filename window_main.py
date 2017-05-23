# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_main.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1269, 632)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AbilityScoreGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.AbilityScoreGroup.setGeometry(QtCore.QRect(10, 60, 401, 531))
        self.AbilityScoreGroup.setAcceptDrops(False)
        self.AbilityScoreGroup.setAutoFillBackground(False)
        self.AbilityScoreGroup.setFlat(False)
        self.AbilityScoreGroup.setCheckable(False)
        self.AbilityScoreGroup.setObjectName("AbilityScoreGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.AbilityScoreGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Label_AbilityScore = QtWidgets.QLabel(self.AbilityScoreGroup)
        self.Label_AbilityScore.setScaledContents(False)
        self.Label_AbilityScore.setObjectName("Label_AbilityScore")
        self.verticalLayout.addWidget(self.Label_AbilityScore)
        self.label_4 = QtWidgets.QLabel(self.AbilityScoreGroup)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.frame_StrengthMod = QtWidgets.QFrame(self.AbilityScoreGroup)
        self.frame_StrengthMod.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_StrengthMod.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_StrengthMod.setObjectName("frame_StrengthMod")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_StrengthMod)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SpinBox_StrengthScore = QtWidgets.QSpinBox(self.frame_StrengthMod)
        self.SpinBox_StrengthScore.setMinimumSize(QtCore.QSize(80, 0))
        self.SpinBox_StrengthScore.setMinimum(8)
        self.SpinBox_StrengthScore.setMaximum(20)
        self.SpinBox_StrengthScore.setObjectName("SpinBox_StrengthScore")
        self.horizontalLayout_2.addWidget(self.SpinBox_StrengthScore)
        self.Label_StrengthScore = QtWidgets.QLabel(self.frame_StrengthMod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_StrengthScore.sizePolicy().hasHeightForWidth())
        self.Label_StrengthScore.setSizePolicy(sizePolicy)
        self.Label_StrengthScore.setMinimumSize(QtCore.QSize(64, 0))
        self.Label_StrengthScore.setObjectName("Label_StrengthScore")
        self.horizontalLayout_2.addWidget(self.Label_StrengthScore)
        self.Label_EchoStrengthMod = QtWidgets.QLabel(self.frame_StrengthMod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_EchoStrengthMod.sizePolicy().hasHeightForWidth())
        self.Label_EchoStrengthMod.setSizePolicy(sizePolicy)
        self.Label_EchoStrengthMod.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Label_EchoStrengthMod.setObjectName("Label_EchoStrengthMod")
        self.horizontalLayout_2.addWidget(self.Label_EchoStrengthMod)
        self.line_6 = QtWidgets.QFrame(self.frame_StrengthMod)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_2.addWidget(self.line_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_strength_saves = QtWidgets.QCheckBox(self.frame_StrengthMod)
        self.checkBox_strength_saves.setMouseTracking(False)
        self.checkBox_strength_saves.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_strength_saves.setCheckable(True)
        self.checkBox_strength_saves.setTristate(False)
        self.checkBox_strength_saves.setObjectName("checkBox_strength_saves")
        self.verticalLayout_2.addWidget(self.checkBox_strength_saves)
        self.checkBox_athletics = QtWidgets.QCheckBox(self.frame_StrengthMod)
        self.checkBox_athletics.setMouseTracking(False)
        self.checkBox_athletics.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_athletics.setCheckable(True)
        self.checkBox_athletics.setTristate(False)
        self.checkBox_athletics.setObjectName("checkBox_athletics")
        self.verticalLayout_2.addWidget(self.checkBox_athletics)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.frame_StrengthMod)
        self.frame_DextMod = QtWidgets.QFrame(self.AbilityScoreGroup)
        self.frame_DextMod.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_DextMod.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_DextMod.setObjectName("frame_DextMod")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_DextMod)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SpinBox_DextScore = QtWidgets.QSpinBox(self.frame_DextMod)
        self.SpinBox_DextScore.setMinimumSize(QtCore.QSize(80, 0))
        self.SpinBox_DextScore.setMinimum(8)
        self.SpinBox_DextScore.setMaximum(20)
        self.SpinBox_DextScore.setObjectName("SpinBox_DextScore")
        self.horizontalLayout_3.addWidget(self.SpinBox_DextScore)
        self.Label_DextScore = QtWidgets.QLabel(self.frame_DextMod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_DextScore.sizePolicy().hasHeightForWidth())
        self.Label_DextScore.setSizePolicy(sizePolicy)
        self.Label_DextScore.setMinimumSize(QtCore.QSize(64, 0))
        self.Label_DextScore.setObjectName("Label_DextScore")
        self.horizontalLayout_3.addWidget(self.Label_DextScore)
        self.Label_EchoDextMod = QtWidgets.QLabel(self.frame_DextMod)
        self.Label_EchoDextMod.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Label_EchoDextMod.setObjectName("Label_EchoDextMod")
        self.horizontalLayout_3.addWidget(self.Label_EchoDextMod)
        self.line_5 = QtWidgets.QFrame(self.frame_DextMod)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_3.addWidget(self.line_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_dexterity_saves = QtWidgets.QCheckBox(self.frame_DextMod)
        self.checkBox_dexterity_saves.setMouseTracking(False)
        self.checkBox_dexterity_saves.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_dexterity_saves.setCheckable(True)
        self.checkBox_dexterity_saves.setTristate(False)
        self.checkBox_dexterity_saves.setObjectName("checkBox_dexterity_saves")
        self.verticalLayout_3.addWidget(self.checkBox_dexterity_saves)
        self.checkBox_sleight_of_hand = QtWidgets.QCheckBox(self.frame_DextMod)
        self.checkBox_sleight_of_hand.setMouseTracking(False)
        self.checkBox_sleight_of_hand.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_sleight_of_hand.setCheckable(True)
        self.checkBox_sleight_of_hand.setTristate(False)
        self.checkBox_sleight_of_hand.setObjectName("checkBox_sleight_of_hand")
        self.verticalLayout_3.addWidget(self.checkBox_sleight_of_hand)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.checkBox_stealth = QtWidgets.QCheckBox(self.frame_DextMod)
        self.checkBox_stealth.setMouseTracking(False)
        self.checkBox_stealth.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_stealth.setCheckable(True)
        self.checkBox_stealth.setTristate(False)
        self.checkBox_stealth.setObjectName("checkBox_stealth")
        self.verticalLayout_9.addWidget(self.checkBox_stealth)
        self.checkBox_acrobatics = QtWidgets.QCheckBox(self.frame_DextMod)
        self.checkBox_acrobatics.setMouseTracking(False)
        self.checkBox_acrobatics.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_acrobatics.setCheckable(True)
        self.checkBox_acrobatics.setTristate(False)
        self.checkBox_acrobatics.setObjectName("checkBox_acrobatics")
        self.verticalLayout_9.addWidget(self.checkBox_acrobatics)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.verticalLayout.addWidget(self.frame_DextMod)
        self.frame_ConstMod = QtWidgets.QFrame(self.AbilityScoreGroup)
        self.frame_ConstMod.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ConstMod.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_ConstMod.setObjectName("frame_ConstMod")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_ConstMod)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SpinBox_ConstScore = QtWidgets.QSpinBox(self.frame_ConstMod)
        self.SpinBox_ConstScore.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SpinBox_ConstScore.sizePolicy().hasHeightForWidth())
        self.SpinBox_ConstScore.setSizePolicy(sizePolicy)
        self.SpinBox_ConstScore.setMinimumSize(QtCore.QSize(80, 0))
        self.SpinBox_ConstScore.setMinimum(8)
        self.SpinBox_ConstScore.setMaximum(20)
        self.SpinBox_ConstScore.setObjectName("SpinBox_ConstScore")
        self.horizontalLayout.addWidget(self.SpinBox_ConstScore)
        self.Label_ConstScore = QtWidgets.QLabel(self.frame_ConstMod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_ConstScore.sizePolicy().hasHeightForWidth())
        self.Label_ConstScore.setSizePolicy(sizePolicy)
        self.Label_ConstScore.setMinimumSize(QtCore.QSize(64, 0))
        self.Label_ConstScore.setObjectName("Label_ConstScore")
        self.horizontalLayout.addWidget(self.Label_ConstScore)
        self.Label_EchoConstMod = QtWidgets.QLabel(self.frame_ConstMod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_EchoConstMod.sizePolicy().hasHeightForWidth())
        self.Label_EchoConstMod.setSizePolicy(sizePolicy)
        self.Label_EchoConstMod.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Label_EchoConstMod.setObjectName("Label_EchoConstMod")
        self.horizontalLayout.addWidget(self.Label_EchoConstMod)
        self.line_4 = QtWidgets.QFrame(self.frame_ConstMod)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_constitution_saves = QtWidgets.QCheckBox(self.frame_ConstMod)
        self.checkBox_constitution_saves.setMouseTracking(False)
        self.checkBox_constitution_saves.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_constitution_saves.setCheckable(True)
        self.checkBox_constitution_saves.setTristate(False)
        self.checkBox_constitution_saves.setObjectName("checkBox_constitution_saves")
        self.verticalLayout_4.addWidget(self.checkBox_constitution_saves)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addWidget(self.frame_ConstMod)
        self.frame_IntelMod = QtWidgets.QFrame(self.AbilityScoreGroup)
        self.frame_IntelMod.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_IntelMod.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_IntelMod.setObjectName("frame_IntelMod")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_IntelMod)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.SpinBox_IntelScore = QtWidgets.QSpinBox(self.frame_IntelMod)
        self.SpinBox_IntelScore.setMinimumSize(QtCore.QSize(80, 0))
        self.SpinBox_IntelScore.setMinimum(8)
        self.SpinBox_IntelScore.setMaximum(20)
        self.SpinBox_IntelScore.setObjectName("SpinBox_IntelScore")
        self.horizontalLayout_4.addWidget(self.SpinBox_IntelScore)
        self.Label_IntelScore = QtWidgets.QLabel(self.frame_IntelMod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_IntelScore.sizePolicy().hasHeightForWidth())
        self.Label_IntelScore.setSizePolicy(sizePolicy)
        self.Label_IntelScore.setMinimumSize(QtCore.QSize(64, 0))
        self.Label_IntelScore.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Label_IntelScore.setObjectName("Label_IntelScore")
        self.horizontalLayout_4.addWidget(self.Label_IntelScore)
        self.Label_EchoIntelMod = QtWidgets.QLabel(self.frame_IntelMod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_EchoIntelMod.sizePolicy().hasHeightForWidth())
        self.Label_EchoIntelMod.setSizePolicy(sizePolicy)
        self.Label_EchoIntelMod.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Label_EchoIntelMod.setObjectName("Label_EchoIntelMod")
        self.horizontalLayout_4.addWidget(self.Label_EchoIntelMod)
        self.line_3 = QtWidgets.QFrame(self.frame_IntelMod)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_4.addWidget(self.line_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox_intelligence_saves = QtWidgets.QCheckBox(self.frame_IntelMod)
        self.checkBox_intelligence_saves.setMouseTracking(False)
        self.checkBox_intelligence_saves.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_intelligence_saves.setCheckable(True)
        self.checkBox_intelligence_saves.setTristate(False)
        self.checkBox_intelligence_saves.setObjectName("checkBox_intelligence_saves")
        self.verticalLayout_5.addWidget(self.checkBox_intelligence_saves)
        self.checkBox_investigation = QtWidgets.QCheckBox(self.frame_IntelMod)
        self.checkBox_investigation.setMouseTracking(False)
        self.checkBox_investigation.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_investigation.setCheckable(True)
        self.checkBox_investigation.setTristate(False)
        self.checkBox_investigation.setObjectName("checkBox_investigation")
        self.verticalLayout_5.addWidget(self.checkBox_investigation)
        self.checkBox_religion = QtWidgets.QCheckBox(self.frame_IntelMod)
        self.checkBox_religion.setMouseTracking(False)
        self.checkBox_religion.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_religion.setCheckable(True)
        self.checkBox_religion.setTristate(False)
        self.checkBox_religion.setObjectName("checkBox_religion")
        self.verticalLayout_5.addWidget(self.checkBox_religion)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.checkBox_arcana = QtWidgets.QCheckBox(self.frame_IntelMod)
        self.checkBox_arcana.setMouseTracking(False)
        self.checkBox_arcana.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_arcana.setCheckable(True)
        self.checkBox_arcana.setTristate(False)
        self.checkBox_arcana.setObjectName("checkBox_arcana")
        self.verticalLayout_8.addWidget(self.checkBox_arcana)
        self.checkBox_nature = QtWidgets.QCheckBox(self.frame_IntelMod)
        self.checkBox_nature.setMouseTracking(False)
        self.checkBox_nature.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_nature.setCheckable(True)
        self.checkBox_nature.setTristate(False)
        self.checkBox_nature.setObjectName("checkBox_nature")
        self.verticalLayout_8.addWidget(self.checkBox_nature)
        self.checkBox_history = QtWidgets.QCheckBox(self.frame_IntelMod)
        self.checkBox_history.setMouseTracking(False)
        self.checkBox_history.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_history.setCheckable(True)
        self.checkBox_history.setTristate(False)
        self.checkBox_history.setObjectName("checkBox_history")
        self.verticalLayout_8.addWidget(self.checkBox_history)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout.addWidget(self.frame_IntelMod)
        self.frame_WisdomMod = QtWidgets.QFrame(self.AbilityScoreGroup)
        self.frame_WisdomMod.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_WisdomMod.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_WisdomMod.setObjectName("frame_WisdomMod")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_WisdomMod)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.SpinBox_WisdomScore = QtWidgets.QSpinBox(self.frame_WisdomMod)
        self.SpinBox_WisdomScore.setMinimumSize(QtCore.QSize(80, 0))
        self.SpinBox_WisdomScore.setMinimum(8)
        self.SpinBox_WisdomScore.setMaximum(20)
        self.SpinBox_WisdomScore.setObjectName("SpinBox_WisdomScore")
        self.horizontalLayout_5.addWidget(self.SpinBox_WisdomScore)
        self.Label_WisdomScore = QtWidgets.QLabel(self.frame_WisdomMod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_WisdomScore.sizePolicy().hasHeightForWidth())
        self.Label_WisdomScore.setSizePolicy(sizePolicy)
        self.Label_WisdomScore.setMinimumSize(QtCore.QSize(64, 0))
        self.Label_WisdomScore.setObjectName("Label_WisdomScore")
        self.horizontalLayout_5.addWidget(self.Label_WisdomScore)
        self.Label_EchoWisdomMod = QtWidgets.QLabel(self.frame_WisdomMod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_EchoWisdomMod.sizePolicy().hasHeightForWidth())
        self.Label_EchoWisdomMod.setSizePolicy(sizePolicy)
        self.Label_EchoWisdomMod.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Label_EchoWisdomMod.setObjectName("Label_EchoWisdomMod")
        self.horizontalLayout_5.addWidget(self.Label_EchoWisdomMod)
        self.line = QtWidgets.QFrame(self.frame_WisdomMod)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_5.addWidget(self.line)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.checkBox_insight = QtWidgets.QCheckBox(self.frame_WisdomMod)
        self.checkBox_insight.setMouseTracking(False)
        self.checkBox_insight.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_insight.setCheckable(True)
        self.checkBox_insight.setTristate(False)
        self.checkBox_insight.setObjectName("checkBox_insight")
        self.verticalLayout_10.addWidget(self.checkBox_insight)
        self.checkBox_medicine = QtWidgets.QCheckBox(self.frame_WisdomMod)
        self.checkBox_medicine.setMouseTracking(False)
        self.checkBox_medicine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_medicine.setCheckable(True)
        self.checkBox_medicine.setTristate(False)
        self.checkBox_medicine.setObjectName("checkBox_medicine")
        self.verticalLayout_10.addWidget(self.checkBox_medicine)
        self.checkBox_perception = QtWidgets.QCheckBox(self.frame_WisdomMod)
        self.checkBox_perception.setMouseTracking(False)
        self.checkBox_perception.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_perception.setCheckable(True)
        self.checkBox_perception.setTristate(False)
        self.checkBox_perception.setObjectName("checkBox_perception")
        self.verticalLayout_10.addWidget(self.checkBox_perception)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox_wisdom_saves = QtWidgets.QCheckBox(self.frame_WisdomMod)
        self.checkBox_wisdom_saves.setMouseTracking(False)
        self.checkBox_wisdom_saves.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_wisdom_saves.setCheckable(True)
        self.checkBox_wisdom_saves.setTristate(False)
        self.checkBox_wisdom_saves.setObjectName("checkBox_wisdom_saves")
        self.verticalLayout_6.addWidget(self.checkBox_wisdom_saves)
        self.checkBox_animal_handling = QtWidgets.QCheckBox(self.frame_WisdomMod)
        self.checkBox_animal_handling.setMouseTracking(False)
        self.checkBox_animal_handling.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_animal_handling.setCheckable(True)
        self.checkBox_animal_handling.setTristate(False)
        self.checkBox_animal_handling.setObjectName("checkBox_animal_handling")
        self.verticalLayout_6.addWidget(self.checkBox_animal_handling)
        self.checkBox_survival = QtWidgets.QCheckBox(self.frame_WisdomMod)
        self.checkBox_survival.setMouseTracking(False)
        self.checkBox_survival.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_survival.setCheckable(True)
        self.checkBox_survival.setTristate(False)
        self.checkBox_survival.setObjectName("checkBox_survival")
        self.verticalLayout_6.addWidget(self.checkBox_survival)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout.addWidget(self.frame_WisdomMod)
        self.frame_CharismaMod = QtWidgets.QFrame(self.AbilityScoreGroup)
        self.frame_CharismaMod.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_CharismaMod.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_CharismaMod.setObjectName("frame_CharismaMod")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_CharismaMod)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.SpinBox_CharismaScore = QtWidgets.QSpinBox(self.frame_CharismaMod)
        self.SpinBox_CharismaScore.setMinimumSize(QtCore.QSize(80, 0))
        self.SpinBox_CharismaScore.setMinimum(8)
        self.SpinBox_CharismaScore.setMaximum(20)
        self.SpinBox_CharismaScore.setObjectName("SpinBox_CharismaScore")
        self.horizontalLayout_6.addWidget(self.SpinBox_CharismaScore)
        self.Label_CharismaScore = QtWidgets.QLabel(self.frame_CharismaMod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_CharismaScore.sizePolicy().hasHeightForWidth())
        self.Label_CharismaScore.setSizePolicy(sizePolicy)
        self.Label_CharismaScore.setMinimumSize(QtCore.QSize(64, 0))
        self.Label_CharismaScore.setObjectName("Label_CharismaScore")
        self.horizontalLayout_6.addWidget(self.Label_CharismaScore)
        self.Label_EchoCharismaMod = QtWidgets.QLabel(self.frame_CharismaMod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_EchoCharismaMod.sizePolicy().hasHeightForWidth())
        self.Label_EchoCharismaMod.setSizePolicy(sizePolicy)
        self.Label_EchoCharismaMod.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Label_EchoCharismaMod.setObjectName("Label_EchoCharismaMod")
        self.horizontalLayout_6.addWidget(self.Label_EchoCharismaMod)
        self.line_2 = QtWidgets.QFrame(self.frame_CharismaMod)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_6.addWidget(self.line_2)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.checkBox_deception = QtWidgets.QCheckBox(self.frame_CharismaMod)
        self.checkBox_deception.setMouseTracking(False)
        self.checkBox_deception.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_deception.setCheckable(True)
        self.checkBox_deception.setTristate(False)
        self.checkBox_deception.setObjectName("checkBox_deception")
        self.verticalLayout_11.addWidget(self.checkBox_deception)
        self.checkBox_persuation = QtWidgets.QCheckBox(self.frame_CharismaMod)
        self.checkBox_persuation.setMouseTracking(False)
        self.checkBox_persuation.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_persuation.setCheckable(True)
        self.checkBox_persuation.setTristate(False)
        self.checkBox_persuation.setObjectName("checkBox_persuation")
        self.verticalLayout_11.addWidget(self.checkBox_persuation)
        self.horizontalLayout_6.addLayout(self.verticalLayout_11)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.checkBox_charisma_saves = QtWidgets.QCheckBox(self.frame_CharismaMod)
        self.checkBox_charisma_saves.setMouseTracking(False)
        self.checkBox_charisma_saves.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_charisma_saves.setCheckable(True)
        self.checkBox_charisma_saves.setTristate(False)
        self.checkBox_charisma_saves.setObjectName("checkBox_charisma_saves")
        self.verticalLayout_7.addWidget(self.checkBox_charisma_saves)
        self.checkBox_intimidation = QtWidgets.QCheckBox(self.frame_CharismaMod)
        self.checkBox_intimidation.setMouseTracking(False)
        self.checkBox_intimidation.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_intimidation.setCheckable(True)
        self.checkBox_intimidation.setTristate(False)
        self.checkBox_intimidation.setObjectName("checkBox_intimidation")
        self.verticalLayout_7.addWidget(self.checkBox_intimidation)
        self.checkBox_performance = QtWidgets.QCheckBox(self.frame_CharismaMod)
        self.checkBox_performance.setMouseTracking(False)
        self.checkBox_performance.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_performance.setCheckable(True)
        self.checkBox_performance.setTristate(False)
        self.checkBox_performance.setObjectName("checkBox_performance")
        self.verticalLayout_7.addWidget(self.checkBox_performance)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout.addWidget(self.frame_CharismaMod)
        self.frame_CharismaMod.raise_()
        self.frame_StrengthMod.raise_()
        self.frame_ConstMod.raise_()
        self.frame_IntelMod.raise_()
        self.frame_WisdomMod.raise_()
        self.frame_DextMod.raise_()
        self.Label_AbilityScore.raise_()
        self.label_4.raise_()
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(390, 10, 341, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ComboBox_Class = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.ComboBox_Class.setObjectName("ComboBox_Class")
        self.horizontalLayout_7.addWidget(self.ComboBox_Class)
        self.ComboBox_Race = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.ComboBox_Race.setObjectName("ComboBox_Race")
        self.horizontalLayout_7.addWidget(self.ComboBox_Race)
        self.ComboBox_Subrace = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.ComboBox_Subrace.setObjectName("ComboBox_Subrace")
        self.horizontalLayout_7.addWidget(self.ComboBox_Subrace)
        self.Label_ProficiencyBonus = QtWidgets.QLabel(self.centralwidget)
        self.Label_ProficiencyBonus.setGeometry(QtCore.QRect(110, 20, 161, 16))
        self.Label_ProficiencyBonus.setObjectName("Label_ProficiencyBonus")
        self.Label_CharLevel = QtWidgets.QLabel(self.centralwidget)
        self.Label_CharLevel.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.Label_CharLevel.setObjectName("Label_CharLevel")
        self.Label_Initiative = QtWidgets.QLabel(self.centralwidget)
        self.Label_Initiative.setGeometry(QtCore.QRect(560, 90, 98, 29))
        self.Label_Initiative.setObjectName("Label_Initiative")
        self.Label_ArmorClass = QtWidgets.QLabel(self.centralwidget)
        self.Label_ArmorClass.setGeometry(QtCore.QRect(680, 90, 97, 29))
        self.Label_ArmorClass.setObjectName("Label_ArmorClass")
        self.Label_MaxHP = QtWidgets.QLabel(self.centralwidget)
        self.Label_MaxHP.setGeometry(QtCore.QRect(800, 90, 131, 29))
        self.Label_MaxHP.setObjectName("Label_MaxHP")
        self.Label_Speed = QtWidgets.QLabel(self.centralwidget)
        self.Label_Speed.setGeometry(QtCore.QRect(450, 90, 98, 29))
        self.Label_Speed.setObjectName("Label_Speed")
        self.SpecialChoiceMenu1 = QtWidgets.QMdiArea(self.centralwidget)
        self.SpecialChoiceMenu1.setGeometry(QtCore.QRect(450, 160, 211, 391))
        self.SpecialChoiceMenu1.setObjectName("SpecialChoiceMenu1")
        self.listWidget_traits = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_traits.setGeometry(QtCore.QRect(680, 160, 251, 171))
        self.listWidget_traits.setObjectName("listWidget_traits")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 140, 73, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(680, 140, 83, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(680, 350, 50, 13))
        self.label_3.setObjectName("label_3")
        self.listWidget_proficiencies = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_proficiencies.setGeometry(QtCore.QRect(960, 160, 256, 171))
        self.listWidget_proficiencies.setObjectName("listWidget_proficiencies")
        self.listWidget_inventory = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_inventory.setGeometry(QtCore.QRect(680, 370, 256, 211))
        self.listWidget_inventory.setObjectName("listWidget_inventory")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(960, 140, 59, 13))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1269, 21))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_new = QtWidgets.QAction(MainWindow)
        self.action_new.setObjectName("action_new")
        self.action_open_file = QtWidgets.QAction(MainWindow)
        self.action_open_file.setObjectName("action_open_file")
        self.actionSpeichern = QtWidgets.QAction(MainWindow)
        self.actionSpeichern.setObjectName("actionSpeichern")
        self.actionSpeichern_unter = QtWidgets.QAction(MainWindow)
        self.actionSpeichern_unter.setObjectName("actionSpeichern_unter")
        self.menuDatei.addAction(self.action_new)
        self.menuDatei.addAction(self.action_open_file)
        self.menuDatei.addAction(self.actionSpeichern)
        self.menuDatei.addAction(self.actionSpeichern_unter)
        self.menubar.addAction(self.menuDatei.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AbilityScoreGroup.setTitle(_translate("MainWindow", "Ability Scores/Modifiers"))
        self.Label_AbilityScore.setText(_translate("MainWindow", "Ability Score Points: 27"))
        self.label_4.setText(_translate("MainWindow", "Ability Scores                              Ability Mod                     Skills"))
        self.Label_StrengthScore.setText(_translate("MainWindow", "Strength"))
        self.Label_EchoStrengthMod.setText(_translate("MainWindow", "-1"))
        self.checkBox_strength_saves.setText(_translate("MainWindow", "Saving Throws"))
        self.checkBox_athletics.setText(_translate("MainWindow", "Athletics"))
        self.Label_DextScore.setText(_translate("MainWindow", "Dexterity"))
        self.Label_EchoDextMod.setText(_translate("MainWindow", "-1"))
        self.checkBox_dexterity_saves.setText(_translate("MainWindow", "Saving Throws"))
        self.checkBox_sleight_of_hand.setText(_translate("MainWindow", "Sleight of Hand"))
        self.checkBox_stealth.setText(_translate("MainWindow", "Stealth"))
        self.checkBox_acrobatics.setText(_translate("MainWindow", "Acrobatics"))
        self.Label_ConstScore.setText(_translate("MainWindow", "Constitution"))
        self.Label_EchoConstMod.setText(_translate("MainWindow", "-1"))
        self.checkBox_constitution_saves.setText(_translate("MainWindow", "Saving Throws"))
        self.Label_IntelScore.setText(_translate("MainWindow", "Intelligence"))
        self.Label_EchoIntelMod.setText(_translate("MainWindow", "-1"))
        self.checkBox_intelligence_saves.setText(_translate("MainWindow", "Saving Throws"))
        self.checkBox_investigation.setText(_translate("MainWindow", "Investigation"))
        self.checkBox_religion.setText(_translate("MainWindow", "Religion"))
        self.checkBox_arcana.setText(_translate("MainWindow", "Arcana"))
        self.checkBox_nature.setText(_translate("MainWindow", "Nature"))
        self.checkBox_history.setText(_translate("MainWindow", "History"))
        self.Label_WisdomScore.setText(_translate("MainWindow", "Wisdom"))
        self.Label_EchoWisdomMod.setText(_translate("MainWindow", "-1"))
        self.checkBox_insight.setText(_translate("MainWindow", "Insight"))
        self.checkBox_medicine.setText(_translate("MainWindow", "Medicine"))
        self.checkBox_perception.setText(_translate("MainWindow", "perception"))
        self.checkBox_wisdom_saves.setText(_translate("MainWindow", "Saving Throws"))
        self.checkBox_animal_handling.setText(_translate("MainWindow", "Animal handling"))
        self.checkBox_survival.setText(_translate("MainWindow", "survival"))
        self.Label_CharismaScore.setText(_translate("MainWindow", "Charisma"))
        self.Label_EchoCharismaMod.setText(_translate("MainWindow", "-1"))
        self.checkBox_deception.setText(_translate("MainWindow", "Deception"))
        self.checkBox_persuation.setText(_translate("MainWindow", "Persuation"))
        self.checkBox_charisma_saves.setText(_translate("MainWindow", "Saving Throws"))
        self.checkBox_intimidation.setText(_translate("MainWindow", "Intimidation"))
        self.checkBox_performance.setText(_translate("MainWindow", "Performance"))
        self.Label_ProficiencyBonus.setText(_translate("MainWindow", "Proficiency Bonus"))
        self.Label_CharLevel.setText(_translate("MainWindow", "Level"))
        self.Label_Initiative.setText(_translate("MainWindow", "Initiative"))
        self.Label_ArmorClass.setText(_translate("MainWindow", "Armor Class"))
        self.Label_MaxHP.setText(_translate("MainWindow", "Max. Hit Point"))
        self.Label_Speed.setText(_translate("MainWindow", "Speed"))
        self.label.setText(_translate("MainWindow", "Special Options"))
        self.label_2.setText(_translate("MainWindow", "Features & Traits"))
        self.label_3.setText(_translate("MainWindow", "Equipment"))
        self.label_5.setText(_translate("MainWindow", "Proficiencies"))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.action_new.setText(_translate("MainWindow", "Neu"))
        self.action_new.setToolTip(_translate("MainWindow", "Neuen Char erstellen"))
        self.action_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_open_file.setText(_translate("MainWindow", "Öffnen"))
        self.action_open_file.setToolTip(_translate("MainWindow", "Bestehende Datei Öffnen"))
        self.action_open_file.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSpeichern.setText(_translate("MainWindow", "Speichern"))
        self.actionSpeichern.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSpeichern_unter.setText(_translate("MainWindow", "Speichern unter"))
        self.actionSpeichern_unter.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))

