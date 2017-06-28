# python qt test program 1
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from window_main import Ui_MainWindow
from CharacterCore import ValueReference, ValueConfig, ValueModifier
import CharacterCore
import acces
print(sys.version_info)
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)



acces.initializeTables(ui)
acces.getValueTable().flushChanges()
MainWindow.show()
sys.exit(app.exec_())
