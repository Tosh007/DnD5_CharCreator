# python qt test program 1
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from window_main import Ui_MainWindow
from CharacterCore import *
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
        data = {"values":{},"choice":{},"ProfChoice":{}}
        values = data["values"]
        choice = data["choice"]
        prof = data["ProfChoice"]
        # values w/o mods
        vdata = acces.getValueTable()._data
        for name in vdata.keys():
            value = vdata[name]
            if isinstance(value, ValueReference):
                values[name] = value.get(True)
        # choices, only need to save state, all dynamic (not connected on init) modifiers are managed by FSMs!
        cdata = acces.getActiveStateTable()
        for name in cdata:
            choice[name] = cdata[name].currentState
        # prof choices seperate, they need to be reconnected to prof values
        for name in getProficiencyTable().table:
            prof[name] = getProficiencyTable().table[name].serialize()
        # finally open save file and dump full data sheet
        f = open(filename,"w")
        yaml.dump(data,f,default_flow_style = False)
        f.close()
    def openFile(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(filter="CharCreator format (*.dnd5)")
        print("open filename: "+filename)
        try:
            f = open(filename,"r")
            data = yaml.load(f)
            f.close()
        except:pass
        values = data["values"]
        choice = data["choice"]
        profs = data["ProfChoice"]
        # values
        DependentObject.blockSignalsGlobal(True)
        for name in values:
            acces.getValue(name).set(values[name])
        # choice/FSMs
        #DependentObject.blockSignalsGlobal(False)#mods can be applied later as well
        for name in choice:
            a = acces.getActiveState(name)
            a.blockProfChoiceInit=True
            try:
                a.widget.setCurrentText(choice[name])
                a.on_changed()  # call manually, signals are blocked and we need the FSM state cycle even if state does not change, to clear ProfChoice
            except AttributeError as e:
                print(e, "occurred while loading choice")
            a.blockProfChoiceInit=False
        # prof choices, deserialize() recreates needed reference to ValueReference.vconf.choice
        #DependentObject.blockSignalsGlobal(True)    # should prevent sideeffects
        for name in profs:
            getProficiencyTable().addChoice(ProficiencyChoice.deserialize(name, profs[name]))
        DependentObject.blockSignalsGlobal(False)
        DependentObject.flushChanges()

storage = storage_()
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

DependentObject.blockSignalsGlobal(True)
acces.initializeTables(ui)
DependentObject.blockSignalsGlobal(False)
DependentObject.flushChanges()
MainWindow.show()

acces.getUI("action_save_file").triggered.connect(storage.saveFile)
acces.getUI("action_open_file").triggered.connect(storage.openFile)

sys.exit(app.exec_())
