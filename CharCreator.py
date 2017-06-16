# python qt test program 1
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
try:
    from window_main import Ui_MainWindow
    from CharacterCore import ValueReference, ValueConfig, ValueModifier
    import CharacterCore
    import acces
except ImportError:
    from program.window_main import Ui_MainWindow
    from program.CharacterCore import ValueReference, ValueConfig, ValueModifier
    import program.CharacterCore as CharacterCore
    import program.acces as acces
print(sys.version_info)
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)



acces.initializeTables(ui)
acces.getValueTable().flushChanges()
MainWindow.show()
sys.exit(app.exec_())
