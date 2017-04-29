# python qt test program 1
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from guitest1 import Ui_MainWindow
import CharacterCore as CharCore


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

