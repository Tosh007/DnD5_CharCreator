# python qt test program 1
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from window_main import Ui_MainWindow
from CharacterCore import ValueReference, ValueConfig, ValueModifier

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

from Values import Values
values = Values(ui)

MainWindow.show()
sys.exit(app.exec_())

