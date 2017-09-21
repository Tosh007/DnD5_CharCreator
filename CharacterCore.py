from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import os

from acces import *
from checkableCombobox import CheckableComboBox
import yaml
def getDirectoryPrefix():
    if os.path.exists("./data"):
        return ""
    else:
        return "program/"

class DependentObject(QObject):
    changeSignal = pyqtSignal()

    @staticmethod
    def getWidgetSignal(widget):
        if isinstance(widget, QtWidgets.QSpinBox):
            return widget.valueChanged
        elif isinstance(widget, CheckableComboBox):
            return widget.view().pressed
        elif isinstance(widget, QtWidgets.QComboBox):
            return widget.currentIndexChanged
        elif isinstance(widget, QtWidgets.QLabel):
            pass
        elif isinstance(widget,QtWidgets.QListWidgetItem):
            pass
        elif isinstance(widget,QtWidgets.QTreeWidgetItem):
            pass
        elif isinstance(widget,QtWidgets.QCheckBox):
            return widget.toggled
        elif (widget is None):pass
        else:
            raise TypeError(str(type(widget))+" is not supported")
    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        s = DependentObject.getWidgetSignal(widget)
        if s:
            s.connect(self.changeSignal)
        self.changeSignal.connect(self.on_changed)

    def connect(self, objects):
        try:
            for obj in objects:
                self.changeSignal.connect(obj.changeSignal)
        except TypeError:
            self.changeSignal.connect(objects.changeSignal)

    def disconnect(self, objects=None):
        if objects:
            try:
                for obj in objects:
                    self.changeSignal.disconnect(obj.changeSignal)
            except TypeError:
                self.changeSignal.disconnect(objects.changeSignal)
        else:
            self.changeSignal.disconnect()

    def on_changed(self,*args,**kw):pass

    def destroy(self):
        DependentObject.getWidgetSignal(self.widget).disconnect(self.changeSignal)
        self.disconnect()

class FiniteStateMachine:
    class AlreadyInTransition(Exception):pass

    stateFile=None
    def initFSM(self):
        self._enterState("Off")

    def __init__(self, states={}):
        self._states = {"Off":{}}
        if self.stateFile:
            f = open(getDirectoryPrefix()+self.stateFile,"r")
            self.states = yaml.load(f)
            f.close()
        self._states.update(self.states)
        self._states.update(states)
        self.props = []
        self.profs = []
        self.currentState = ""

    def request(self,state):
        assert state in self._states
        if self.currentState is None:
            raise self.AlreadyInTransition(str(type(self)))
        self._exitState()
        self._enterState(state)

    def _exitState(self):
        state = self.currentState
        self.currentState = None
        for key in self._states[state]:
            if key=="mod":
                modifiers = self._states[state][key]
                for mod in modifiers:
                    targets = getValues(modifiers[mod])
                    mod = getModifier(mod)
                    mod.disconnect(targets)
            elif key=="depend":
                dependants = self._states[state][key]
                for dep in dependants:
                    dep = getValues(name)[0]
                    targets = getValues(dependants[name])
                    dep.disconnect(targets)
        ui = getUI("listWidget_traits")
        for item in self.props:
            i=ui.takeItem(ui.row(item))
            assert i==item
        for choice in self.profs:
            getProficiencyTable().removeChoice(choice)
        self.profs.clear()
        self.props.clear()
        state = state.replace("-","_")
        state = state.replace(" ","_")
        self.exit(state)
        if hasattr(self,"exit"+state):
            getattr(self, "exit"+state)()

    def _enterState(self,state):
        ui = getUI("listWidget_traits")
        for key in self._states[state]:
            if key=="mod":
                modifiers = self._states[state][key]
                for mod in modifiers:
                    targets = getValues(modifiers[mod])
                    mod = getModifier(mod)
                    mod.connect(targets)
            elif key=="depend":
                dependants = self._states[state][key]
                for name in dependants:
                    dep = getValues(name)[0]
                    targets = getValues(dependants[name])
                    dep.connect(targets)
            elif key=="property":
                for name in self._states[state][key]:
                    ui.addItem(name)
                    item = ui.item(ui.count()-1)
                    self.props.append(item)
            elif key=="ProfChoice":
                choices = self._states[state][key]
                for choice in choices:
                    choice = tuple(choice.values())[0]
                    n = choice["n"]
                    profs = choice["profs"]
                    c = ProficiencyChoice(n, profs)
                    name = str(c)
                    self.profs.append(name)
                    getProficiencyTable().addChoice(c)
                    getUI("treeWidget_proficiencies").itemClicked.emit(None,0)
        nstate = state.replace("-","_")
        nstate = nstate.replace(" ","_")
        self.enter(nstate)
        if hasattr(self,"enter"+nstate):
            getattr(self, "enter"+nstate)()
        self.currentState = state
    def exit(self,state):pass
    def enter(self,state):pass


class ValueReference(DependentObject):
    # reference to a value stored within a qt widget
    def __init__(self, widget, valueconfig, format=None):
        super().__init__(widget)
        self.vconf = valueconfig
        self.format = format
        self.modifiers = []
        self._blockSignals = None
        self.lastValue = 0
        if isinstance(widget, QtWidgets.QSpinBox):
            self._get = widget.value
            self._set = widget.setValue
            self._blockSignals = widget.blockSignals
        elif isinstance(widget, QtWidgets.QLabel):
            self._get = 0
            self._set = widget.setText
        elif isinstance(widget, QtWidgets.QListWidgetItem) or isinstance(widget,QtWidgets.QTreeWidgetItem):
            self._get = 0
            self._set = (self.widget.setText if isinstance(widget, QtWidgets.QListWidgetItem) else lambda text:self.widget.setText(0,text))
            if valueconfig.forceCheckbox:
                if isinstance(widget, QtWidgets.QListWidgetItem):
                    widget = widget.listWidget()
                else:
                    widget = widget.treeWidget()
                widget.itemClicked.connect(self.changeSignal)
                self.widget.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                try:
                    self.widget.setCheckState(Qt.Unchecked)
                except TypeError:
                    self.widget.setCheckState(0,Qt.Unchecked)
                self.previousCheckState = Qt.Unchecked
        elif isinstance(widget,QtWidgets.QCheckBox):
            self._get = self.widget.isChecked
            self._set = self.widget.setChecked
            self._blockSignals = self.widget.blockSignals
        elif widget is None:
            self._get = 0
        else:
            raise TypeError("unsupported widget "+str(type(widget)))
        if self.vconf.VisualUpdateSignal:
            getValue(self.vconf.VisualUpdateSignal).changeSignal.connect(self.on_visual_update)

    def __iadd__(self,other):
        assert type(other) is int
        if other==0:return self
        self.set(self.get(True)+other)
        #self.changeSignal.emit()
        return self

    def __isub__(self,other):
        assert type(other) is int
        if other==0:return self
        self.set(self.get(True)-other)
        #self.changeSignal.emit()
        return self

    def set(self, value, setLastValue=True):
        v, mstring = self.applyMods(value, True)
        if setLastValue:
            self.lastValue = self.get()
        if not callable(self._get):
            self._get = value
        self.showValue(value,v,mstring)

    def reset(self):
        self.set(self.lastValue, False)

    def get(self, ignoreModifier=False):
        # returns current value from qt widget
        if isinstance(self._get, str):
            v = int(self._get)
        elif isinstance(self._get, int):
            v = self._get
        else:
            v = int(self._get())
        if not ignoreModifier:
            v = self.applyMods(v)
        return v

    def applyMods(self, v, needDescription=False):
        mstring = ""
        self.modifiers.sort(key=ValueModifier.modOrder)
        for mod in self.modifiers:
            nv = mod.mod(v)
            if (nv!=v): mstring += mod.string(v)+"\n"  # only add mod desc to mstring if value is changed
            v = nv
        mstring = mstring[:-1]
        if not needDescription:return v
        else:return (v,mstring)

    def on_changed(self):
        # always called when value is changed by gui, or another value changed that may cause this to change
        # uses ValueConfig to verify such a value is possible,
        # and either updates the fallback value, or resets to fallback
        # exception: if valueconfig.getMaxValue the value is just set to the highest possible value.
        if self.vconf.alwaysMax:
            maxv = self.vconf.getMaxValue(self.lastValue)
            self.set(maxv)
            return
        value = self.get(True)
        if self.vconf.forceCheckbox:
            try:
                checkState = self.widget.checkState()
            except TypeError:
                checkState = self.widget.checkState(0)
            if checkState == Qt.Checked and self.get()==value:
                value=1
            else:
                value=0
        closest = self.vconf.checkRequirements(value, self.lastValue)
        v, mstring = self.applyMods(closest, True)
        if self.vconf.getMaxValue:
            maxValue=self.vconf.getMaxValue(self.lastValue)
        else:
            maxValue=None
        self.lastValue = closest
        self.showValue(closest,v,mstring,maxValue)

    def on_visual_update(self):
        self.widget.setHidden(self.canBeHidden())

    def showValue(self,v,vmod,mdesc,maxValue=None):
        if not maxValue:maxValue=v
        svmod = " ({0})".format(vmod)
        if self._blockSignals:
            self._blockSignals(True)
        if isinstance(self.widget, QtWidgets.QLabel) or isinstance(self.widget, QtWidgets.QListWidgetItem) or isinstance(self.widget, QtWidgets.QTreeWidgetItem):
            if self.format:s = self.format.format(v,(svmod if mdesc else ""),vmod)
            else:s=str(v) + (svmod if mdesc else "")
            self._set(s)
        elif isinstance(self.widget, QtWidgets.QSpinBox):
            self.widget.setSuffix((svmod if mdesc else ""))
            self._set(v)
        elif isinstance(self.widget, QtWidgets.QCheckBox):
            b = bool(vmod)
            self._set(b)
        if self.vconf.forceCheckbox:
            if vmod:
                b=Qt.Checked
                self.previousCheckState = Qt.Checked
            else:
                b=Qt.Unchecked
                self.previousCheckState = Qt.Unchecked
            try:
                self.widget.setCheckState(b)
            except TypeError:
                self.widget.setCheckState(0,b)
        try:

            if self.widget:
                self.widget.setHidden(self.vconf.hide(v,vmod,maxValue))
                if self.vconf.setToolTip:
                    try:
                        self.widget.setToolTip(mdesc)
                    except TypeError:
                        self.widget.setToolTip(0,mdesc)
            self.vconf.specialSetup(self, v, vmod, mdesc, maxValue)
            if self._blockSignals:
                self._blockSignals(False)

        except TypeError as e:
            raise e

    def canBeHidden(self):
        v = self.get(True)
        vmod, mstring= self.applyMods(v,True)
        if self.vconf.getMaxValue:
            maxValue = self.vconf.getMaxValue(self.lastValue)
        else:
            maxValue=0
        return self.vconf.hide(v,vmod,maxValue)

class ValueConfig:
    @staticmethod
    def checkRequirements(value, oldvalue):
        return oldvalue
    getMaxValue = None
    alwaysMax = False
    forceCheckbox = False
    VisualUpdateSignal = None
    setToolTip = True
    hide=lambda v,vmod,maxV:False
    specialSetup = lambda widget,v,vmod,mdesc,maxValue=None: None# a special ui setup sequence


class ValueConfig_allow(ValueConfig):
    @staticmethod
    def checkRequirements(value, oldvalue):
        return value


class ValueModifier:
    # now using linear id counter upon instance creation for dict identification
    _ID = 0
    def __init__(self,mod,text,order=0):
        self.mod = mod
        self.text = text
        self.order = order
        self.ID = self._ID
        ValueModifier._ID+=1

    def connect(self, valueref):
        try:
            for ref in valueref:
                ref.modifiers.append(self)
                ref.changeSignal.emit()
        except TypeError:
            valueref.modifiers.append(self)
            valueref.changeSignal.emit()

    def disconnect(self, valueref, try_=False):
        try:
            try:
                for ref in valueref:
                        ref.modifiers.remove(self)
                        ref.changeSignal.emit()
            except TypeError:
                valueref.modifiers.remove(self)
                valueref.changeSignal.emit()
        except ValueError as e:
            if not try_:
                raise ValueError from e

    def modOrder(m):
        return m.order

    def string(self,v=None):
        if v is None:
            return self.text.format("","","")
        else:
            mv = self.mod(v)
            dv = mv-v
            return self.text.format(v,mv,dv)

    def __hash__(self):
        return hash(self.ID)

    def __eq__(self, other):
        return self.ID==other.ID


class ChoiceReference(FiniteStateMachine, DependentObject):
    usePrerequisite = False
    def __init__(self, widget, states={}):
        if self.usePrerequisite:
            states.update({"None":{}})
        FiniteStateMachine.__init__(self,states)
        if self.usePrerequisite:
            assert "None" in self._states
        if self.usePrerequisite:
            widget.addItem("None")
            for state in self._states:
                if "prerequisite" in self._states[state].keys():
                    self._states[state]["prerequisite"] = eval("lambda: "+self._states[state]["prerequisite"])
                else:
                    self._states[state]["prerequisite"] = lambda: True
        widget.addItems(sorted(self.states.keys(),key=str.lower))
        DependentObject.__init__(self, widget)
        self.initFSM()
        self.on_changed()

    def on_changed(self):
        item = self.widget.currentText()
        if self.usePrerequisite:
            for state in self._states:
                if state=="Off":continue
                enabled = self._states[state]["prerequisite"]()
                index = self.widget.findText(state)
                self.widget.model().item(index).setEnabled(enabled)
            #if item=="None":
            #    self.request("Off")
            if item == self.currentState:
                if not self._states[item]["prerequisite"]():
                    self.widget.setCurrentIndex(0)
                    self.request("None")
            elif self.currentState:
                self.request(item)
        else:
            self.request(item)

    def destroy(self):
        self.request("Off")
        self.widget.disconnect()
        self.changeSignal.disconnect()
        self.widget.clear()


class ProficiencyChoice:
    def __init__(self, n, profs):
        self.maxN = n
        profs_ = list(profs)
        for prof in profs:
            profs_ += tuple(getProficiencyTable().getChildProficiencies(prof))
        self.profs = {p:0 for p in profs_}   # lastValue associated with this choice element

    def __str__(self):
        s = "prof_" + str(self.maxN)
        for i in sorted(self.profs.keys(), key=str.lower):
            s += "_"+i
        return s

    def proficient(self,name, v):
        if str(self) not in getProficiencyTable().table.keys():return 0
        if name not in self.profs.keys():
            return 0
        if self.profs[name] == v:   # nothing changed
            return v
        elif self.profs[name] > v:
            assert self.profs[name]==1 and v==0 # assume bool
            self.profs[name] = v
            getValue("listWidget_proficiencies_VisualUpdate").changeSignal.emit()
            return v
        elif self.profs[name] < v:
            assert self.profs[name]==0 and v==1
            if self.maxN - self.getUsedPoints() > 0:
                self.profs[name] = v#1
                getValue("listWidget_proficiencies_VisualUpdate").changeSignal.emit()
                return v
            else:
                return self.profs[name]
        else:
            raise ValueError("invalid case for ProficiencyChoice!")

    def possible(self,name,v):
        if str(self) not in getProficiencyTable().table.keys():
            return 0
        if name not in self.profs.keys():
            return 0
        else:
            return self.maxN - self.getUsedPoints() + self.profs[name]

    def getUsedPoints(self):
        return sum(self.profs.values())

class BaseMenu:
    typename = "BaseMenu"
