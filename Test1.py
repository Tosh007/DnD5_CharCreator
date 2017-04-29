# python qt test program 1
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from guitest1 import Ui_MainWindow
from CharacterCore import ValueReference, ValueConfig, ValueModifier

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

class AbilityScoreConfig(ValueConfig):
    points = ValueReference("AbilityScorePoints", ui.Label_AbilityScore, ValueConfig, 27, "Ability Score Points: {0}")
    @staticmethod
    def checkRequirements(value, oldvalue):
        total = AbilityScoreConfig.points.get() - AbilityScoreConfig.getReqPoints(value) + AbilityScoreConfig.getReqPoints(oldvalue)
        print(total if total>0 else 0)
        if (total>=0):
            AbilityScoreConfig.points.set(total)
            return True
        return False
    @staticmethod
    def getReqPoints(value):
        assert (value>=8)
        if (value>15):return 100
        return (0,1,2,3,4,5,7,9)[value-8]


strength     = ValueReference("StrengthScore", ui.SpinBox_StrengthScore, AbilityScoreConfig)
dexterity    = ValueReference("DexterityScore", ui.SpinBox_DextScore, AbilityScoreConfig)
constitution = ValueReference("ConstitutionScore", ui.SpinBox_ConstScore, AbilityScoreConfig)
intelligence = ValueReference("IntelligenceScore", ui.SpinBox_IntelScore, AbilityScoreConfig)
wisdom       = ValueReference("WisdomScore", ui.SpinBox_WisdomScore, AbilityScoreConfig)
charisma     = ValueReference("CharismaScore", ui.SpinBox_CharismaScore,AbilityScoreConfig)


MainWindow.show()
sys.exit(app.exec_())

