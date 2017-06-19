from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
import os
try:
    from acces import *
except ImportError:
    from program.acces import *
import yaml
def getDirectoryPrefix():
    if os.path.exists("./data"):
        return ""
    else:
        return "program/"

class DependentObject(QObject):
    changeSignal = pyqtSignal()
    def __init__(self, widget):
        super().__init__(widget)
        self.widget = widget
        if isinstance(widget, QtWidgets.QSpinBox):
            widget.valueChanged.connect(self.changeSignal)
        elif isinstance(widget, QtWidgets.QComboBox):
            widget.currentIndexChanged.connect(self.changeSignal)
        elif isinstance(widget, QtWidgets.QLabel):
            pass
        elif isinstance(widget,QtWidgets.QListWidget):
            pass
        elif isinstance(widget,QtWidgets.QCheckBox):
            widget.toggled.connect(self.changeSignal)
        elif (widget is None):pass
        else:
            raise TypeError(str(type(widget))+" is not supported")
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

class FiniteStateMachine:
    stateFile=None
    _states = {"Off":{}}
    def initFSM(self):
        self._enterState("Off")

    def __init__(self, states={}):
        if self.stateFile:
            f = open(getDirectoryPrefix()+self.stateFile,"r")
            self.states = yaml.load(f)
            f.close()
        self._states.update(self.states)
        self._states.update(states)
        self.props = []
        self.currentState = ""

    def request(self,state):
        assert state in self._states
        #print(str(type(self))+":state:"+state)
        self._exitState(self.currentState)
        self._enterState(state)

    def _exitState(self,state):
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
        self.item = None
        if isinstance(widget, QtWidgets.QSpinBox):
            self._get = widget.value
            self._set = widget.setValue
            self._blockSignals = widget.blockSignals
        elif isinstance(widget, QtWidgets.QLabel):
            self._get = 0
            self._set = widget.setText
        elif isinstance(widget, QtWidgets.QListWidget):
            self.widget = QtWidgets.QListWidgetItem("")
            self._get = 0
            self._set = self.widget.setText
            widget.addItem(self.widget)
        elif isinstance(widget,QtWidgets.QCheckBox):
            self._get = self.widget.isChecked
            self._set = self.widget.setChecked
            self._blockSignals = widget.blockSignals
        elif widget is None:
            self._get = 0
        else:
            raise TypeError("unsupported widget "+str(type(widget)))
        self.lastValue = 0

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
            #print(v)
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
        #if type(self.widget)is QtWidgets.QCheckBox:
            #print("changed:",self.widget.isChecked())
        if self.vconf.getMaxValue:
            maxv = self.vconf.getMaxValue()
            self.set(maxv)
            return
        value = self.get(True)
        if self.vconf.checkRequirements(value, self.lastValue):
            self.lastValue = value
            v, mstring = self.applyMods(value, True)
            self.showValue(value,v,mstring)
        else:
            self.reset()

    def showValue(self,v,vmod,mdesc):
        svmod = " ({0})".format(vmod)
        if self._blockSignals:
            self._blockSignals(True)
        if isinstance(self.widget, QtWidgets.QLabel) or isinstance(self.widget, QtWidgets.QListWidgetItem):
            if self.format:s = self.format.format(v,(svmod if mdesc else ""),vmod)
            else:s=str(v) + (svmod if mdesc else "")
            self._set(s)
        elif isinstance(self.widget, QtWidgets.QSpinBox):
            self.widget.setSuffix((svmod if mdesc else ""))
            self._set(v)
        elif isinstance(self.widget, QtWidgets.QCheckBox):
            b = bool(vmod)
            self._set(b)
        self.widget.setHidden(self.vconf.hide(vmod))
        self.widget.setToolTip(mdesc)
        if self._blockSignals:
            self._blockSignals(False)


class ValueConfig:
    @staticmethod
    def checkRequirements(value, oldvalue):
        return False
    getMaxValue = None
    hide=lambda s,v=0:False


class ValueConfig_allow(ValueConfig):
    @staticmethod
    def checkRequirements(value, oldvalue):
        return True


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

    def disconnect(self, valueref):
        try:
            for ref in valueref:
                ref.modifiers.remove(self)
                ref.changeSignal.emit()
        except TypeError:
            valueref.modifiers.remove(self)
            valueref.changeSignal.emit()

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
    def __init__(self, widget, states={}):
        FiniteStateMachine.__init__(self,states)
        DependentObject.__init__(self, widget)
        self.initFSM()
        widget.addItems(sorted(self.states.keys(),key=str.lower))
        self.on_changed()

    def on_changed(self):
        item = self.widget.currentText()
        self.request(item)

    def destroy(self):
        self.request("Off")
        self.widget.disconnect()
        self.changeSignal.disconnect()
        self.widget.clear()


class Proficiency(DependentObject):
    def __init__(self, name, parent, valueref):
        super().__init__(None)
        self.name = name
        self.parent = parent
        self.value = valueref
        self.subTypes = []
        valueref.connect(self)
        valueref.set(0)
        if parent:
            parent.connect(self)

    #check if other proficiency has self in parent chain
    def contains(self, other):
        while other:
            if other == self:
                return True
            other = other.parent
        return False

    def set(self,v):
        if self.value.get()!=v:
            self.value.set(v)
            self.changeSignal.emit()

    def get(self):
        v=self.value.get()
        if self.parent:
            p=self.parent.get()
        else:p=False
        return (1 if v or p else 0)
