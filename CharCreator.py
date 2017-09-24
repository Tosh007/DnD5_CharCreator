# main file
# top-level control
# anything that does not fit anywhere else
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

    def updateWindowTitle(self):
        MainWindow.setWindowTitle("DND5e CharCreator - " + (self.currentSaveName if self.currentSaveName else "no file"))

    def saveFile(self, saveAs=False):
        if saveAs or not self.currentSaveName:
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(filter="CharCreator format (*.dnd5)")
        else:
            filename = self.currentSaveName
        if not filename:return
        self.currentSaveName = filename
        print("save filename: "+filename)
        data = {"values":{},"choice":{},"ProfChoice":{},"multiChoice":{}}
        values = data["values"]
        choice = data["choice"]
        prof = data["ProfChoice"]
        multiChoice = data["multiChoice"]
        # values, no mods
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
        # multi choice (2 scores +1) next
        cdata = acces.getActiveMultiStateTable()
        for name in cdata:
            multiChoice[name] = tuple(cdata[name].widget._checkedItems)
        # finally open save file and dump full data sheet
        try:
            f = open(filename,"w")
            yaml.dump(data,f)#,default_flow_style = False)
            f.close()
        except BaseException as e:
            print("saving somehow failed because", e)
        self.updateWindowTitle()
    def openFile(self, filename = None):
        if not filename:
            filename, _ = QtWidgets.QFileDialog.getOpenFileName(filter="CharCreator format (*.dnd5)")
        if not filename:return
        print("open filename: "+filename)
        try:
            f = open(filename,"r")
            data = yaml.load(f)
            f.close()
        except BaseException as e:
            print("save opening failed because", e)
            return
        values = data["values"]
        choice = data["choice"]
        profs = data["ProfChoice"]
        multiChoice = data["multiChoice"]
        # values
        DependentObject.blockSignalsGlobal(True)
        for name in values:
            acces.getValue(name).set(values[name])
        # choice/FSMs
        s = list(choice)
        s.sort(key=lambda x: getState(x).loadLevel)
        for name in s:
            print(name,choice[name])
            a = acces.getActiveState(name)
            a.blockProfChoiceInit=True
            try:
                if type(a.widget) is QtWidgets.QCheckBox:
                    a.widget.setCheckState(QtCore.Qt.Checked if choice[name]=="Checked" else QtCore.Qt.Unchecked)
                    # no idea why (?!) but this updates automatically, and throws an error if we do so twice
                else:
                    a.widget.setCurrentText(choice[name])
                    a.on_changed()  # call manually, signals are blocked and we need the FSM state cycle even if state does not change, to clear ProfChoice
            except AttributeError as e:
                if not type(a) is getState("PrimaryState"):
                    print(type(a))
                    raise e
            a.blockProfChoiceInit=False
        # ProfChoice
        for name in profs:
            getProficiencyTable().addChoice(ProficiencyChoice.deserialize(name, profs[name]))
        # multiChoice
        for name in multiChoice:
            print(name,multiChoice[name])
            choice = getActiveMultiState(name)
            widget = choice.widget
            widget.setAllChecked(False)
            # set checkState according to list
            for item in multiChoice[name]:
                widget.setItemWithNameChecked(item,True)
            choice.on_changed()
        self.currentSaveName = filename
        if filename == "data/character/newSave.yaml":
            self.currentSaveName = None
        DependentObject.blockSignalsGlobal(False)
        DependentObject.flushChanges()
        self.updateWindowTitle()

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

acces.getUI("action_save_file").triggered.connect(lambda: storage.saveFile(False))
acces.getUI("action_open_file").triggered.connect(storage.openFile)
acces.getUI("action_saveAs_file").triggered.connect(lambda: storage.saveFile(True))
acces.getUI("action_new").triggered.connect(lambda: storage.openFile("data/character/newSave.yaml"))

storage.updateWindowTitle()

sys.exit(app.exec_())
