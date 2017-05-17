from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject

class DependentObject(QObject):
    changeSignal = pyqtSignal()
    def __init__(self, widget):
        QObject.__init__(self, widget)
        print(str(type(self))+".init")
        self.widget = widget
        if isinstance(widget, QtWidgets.QSpinBox):
            widget.valueChanged.connect(self.changeSignal)
        elif isinstance(widget, QtWidgets.QComboBox):
            widget.currentIndexChanged.connect(self.changeSignal)
        elif isinstance(widget, QtWidgets.QLabel):
            pass
        else:
            raise TypeError(str(type(widget))+" is not supported")
        self.changeSignal.connect(self.on_changed)

    def connect(self, objects):
        try:
            for obj in objects:
                self.changeSignal.connect(obj.changeSignal)
        except TypeError:
            self.changeSignal.connect(objects.changeSignal)

    def disconnect(self, objects):
        try:
            for obj in objects:
                self.changeSignal.disconnect(obj.changeSignal)
        except TypeError:
            self.changeSignal.disconnect(objects.changeSignal)

    def __del__(self):
        print(str(type(self))+".del")

class FiniteStateMachine:
    _states = {"Off":{}}
    def initFSM(self):
        self._enterState("Off")

    def __init__(self, objects):
        self._states.update(self.states)
        self.objects = objects
        self.currentState = ""

    def request(self,state):
        assert state in self._states
        print(str(type(self))+":state:"+state)
        self._exitState(self.currentState)
        self._enterState(state)

    def _exitState(self,state):
        self.currentState = None
        for key in self._states[state]:
            if key=="mod":
                modifiers = self._states[state][key]
                for mod in modifiers:
                    targets = self.objects.get(modifiers[mod])
                    mod.disconnect(targets)
            elif key=="depend":
                dependants = self._states[state][key]
                for dep in dependants:
                    targets = self.objects.get(dependants[dep])
                    dep.disconnect(targets)
        if hasattr(self,"exit"+state):
            getattr(self, "exit"+state)()

    def _enterState(self,state):
        for key in self._states[state]:
            if key=="mod":
                modifiers = self._states[state][key]
                for mod in modifiers:
                    targets = self.objects.get(modifiers[mod])
                    mod.connect(targets)
            elif key=="depend":
                dependants = self._states[state][key]
                for name in dependants:
                    dep = self.objects.get(name)[0]
                    targets = self.objects.get(dependants[name])
                    dep.connect(targets) 
        if hasattr(self,"enter"+state):
            getattr(self, "enter"+state)()
        self.currentState = state


class ValueReference(DependentObject):
    # reference to a value stored within a qt widget
    def __init__(self, widget, valueconfig, format=None):
        DependentObject.__init__(self,widget)
        self.vconf = valueconfig
        self.format = None
        self.modifiers = []
        if isinstance(widget, QtWidgets.QSpinBox):
            self._get = widget.value
            self._set = widget.setValue
            self._blockSignals = widget.blockSignals
        elif isinstance(widget, QtWidgets.QLabel):
            self._get = 0
            self._set = widget.setText
            self.format = format
            self._blockSignals = None
        else:
            raise NotImplemented("unsupported widget")
        self.lastValue = self.get()

    def set(self, value):
        v, mstring = self.applyMods(value, True)
        if not callable(self._get):
            self._get = value
        self.showValue(value,v,mstring) 
        
    def get(self, ignoreModifier=False):
        # returns current value from qt widget
        if isinstance(self._get, str):
            v = int(self._get)
        elif isinstance(self._get, int):
            v = self._get
        else: 
            v = self._get()
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
        if self.vconf.getMaxValue:
            maxv = self.vconf.getMaxValue()
            self.set(maxv)
            return
        value = self.get(True)
        if self.vconf.checkRequirements(value, self.lastValue):
            self.lastValue = value
        else:
            self.set(self.lastValue)
            value = self.lastValue
        v, mstring = self.applyMods(value, True)
        self.showValue(value,v,mstring)

    def showValue(self,v,vmod,mdesc):
        svmod = " ({0})".format(vmod)
        
        if isinstance(self.widget, QtWidgets.QLabel):
            if self.format:sv = self.format.format(v,(svmod if mdesc else ""),vmod)
            else:sv=str(v) + (svmod if mdesc else "")
            s = sv
            self._set(s)
        elif isinstance(self.widget, QtWidgets.QSpinBox):
            self.widget.setSuffix((svmod if mdesc else ""))
            self._set(v)
        self.widget.setToolTip(mdesc)

class ValueConfig:
    @staticmethod
    def checkRequirements(value, oldvalue):
        return False

    getMaxValue = None


class ValueModifier:
    # now using linear id counter upon instance creation for dict identification
    _ID = 0
    def __init__(self,mod,text,order=0):
        self.mod = mod
        self.text = text
        self.order = order
        self.ID = self._ID
        ValueModifier._ID+=1
        print (str(type(self))+":"+str(self.ID))

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
    def __init__(self, widget, values):
        widget.addItems(sorted(self.states.keys(),key=str.lower))
        FiniteStateMachine.__init__(self, values)
        DependentObject.__init__(self, widget)
        self.initFSM()
        self.on_changed()

    def on_changed(self):
        item = self.widget.currentText()
        self.request(item)

    def destroy(self):
        self.request("Off")
        self.widget.disconnect()
        self.changeSignal.disconnect()
        self.widget.clear()
