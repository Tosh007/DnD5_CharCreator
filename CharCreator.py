# python qt test program 1
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from window_main import Ui_MainWindow
from CharacterCore import ValueReference, ValueConfig, ValueModifier
import CharacterCore
import acces
import yaml
print(sys.version_info)

class storage_:
    def __init__(self):
        self.newName = "data/character/new.yaml"
        self.currentSaveName = None
    def saveFile(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(filter="CharCreator format (*.dnd5)")
        print("save filename: "+filename)
        data = {"values":{},"choice":{}}
        values = data["values"]
        choice = data["choice"]
        vdata = acces.getValueTable()._data
        for name in vdata.keys():
            value = vdata[name]
            if isinstance(value, CharacterCore.ValueReference):
                values[name] = value.get(True)
                f = open(filename,"w")
                yaml.dump(data,f,default_flow_style = False)
                f.close()
    def openFile(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName()
        print("open filename: "+filename)

storage = storage_()
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

acces.initializeTables(ui)
acces.getValueTable().flushChanges()
MainWindow.show()

acces.getUI("action_save_file").triggered.connect(storage.saveFile)
acces.getUI("action_open_file").triggered.connect(storage.openFile)

sys.exit(app.exec_())
