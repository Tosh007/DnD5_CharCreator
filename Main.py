# python qt test program 1
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from window_main import Ui_MainWindow
from CharacterCore import ValueReference, ValueConfig, ValueModifier
print(sys.version_info)
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
from guiSetup import setup_main_window
setup_main_window(ui)

from Values import Values
values = Values(ui)
values.request("On")

MainWindow.show()
sys.exit(app.exec_())

