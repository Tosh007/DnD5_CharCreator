from PyQt5 import QtCore, QtGui, QtWidgets
from direct.fsm.FSM import FSM

class DependentObject:
    def __init__(self, widget):
        self.widget = widget
        if isinstance(widget, QtWidgets.QSpinBox):
            self.changeSignal = widget.valueChanged
        elif isinstance(widget, QtWidgets.QComboBox):
            self.changeSignal = widget.currentIndexChanged
        elif isinstance(widget, QtWidgets.QLabel):
            self.changeSignal = None
        else:
            raise TypeError(str(type(widget))+" is not supported")

    def connectChange(self, objects):
        if iter(objects):
            for obj in objects:
                self.changeSignal.connect(obj.changeSignal)
        else:
            self.changeSignal.connect(objects)

    def disconnectChange(self, objects):
        if iter(objects):
            for obj in objects:
                self.changeSignal.disconnect(obj.changeSignal)
        else:
            self.changeSignal.disconnect(objects)


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
        
        if self.changeSignal:
            self.changeSignal.connect(self.on_changed)
        self.lastValue = self.get()

    def set(self, value):
        if not callable(self._get):
            self._get = value
        if self.format:
            value = self.format.format(value)
        if self._blockSignals:
            self._blockSignals(True)
        self._set(value)
        if self._blockSignals:
            self._blockSignals(False)
        
        v, mstring = self.applyMods(value, True)
        if (isinstance(self.widget, QtWidgets.QSpinBox)):
            self.widget.setSuffix(mstring)
        

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
                nv = mod.mod(v)
                if (nv!=v): mstring += " "+mod.string()  # only add mod desc to mstring if value is changed
                v = nv
        if not needDescription:return v
        else:return (v,mstring)

    def on_changed(self):
        # always called when value is changed by gui
        # uses ValueConfig to verify such a value is possible,
        # and either updates the fallback value, or resets to fallback
        value = self.get(True)
        if self.vconf.checkRequirements(value, self.lastValue):
            self.lastValue = value
        else:
            self.set(self.lastValue)
        v, mstring = self.applyMods(value,True)
        if (isinstance(self.widget, QtWidgets.QSpinBox)):
            self.widget.setSuffix(mstring)

# Deprecated, to be replaced
class DependantValueReference(ValueReference):
    # this value should not be set by UI
    def __init__(self, widget, valueconfig, format=None):
        assert(isinstance(widget, QtWidgets.QLabel))
        ValueReference.__init__(self,widget,valueconfig,format)
        self.vconf.dependant_value_change.connect(self.on_dependant_change)

    def on_dependant_change(self):
        maxv = self.vconf.getMaxValue()
        self.set(maxv)


class ValueConfig:
    @staticmethod
    def checkRequirements(value, oldvalue):
        return False

    @staticmethod
    def getMaxValue():
        return -1



class ValueModifier:
    mod = lambda x: x
    order = 0
    text = "Null mod"

    @classmethod
    def connect(self, valueref):
        if iter(valueref):
            for ref in valueref:
                ref.modifiers.append(self)
                ref.changeSignal.emit(0)
        else:
            valueref.modifiers.append(self)
            valueref.changeSignal.emit(0)

    @classmethod
    def disconnect(self, valueref):
        if iter(valueref):
            for ref in valueref:
                ref.modifiers.remove(self)
        else:
            valueref.modifiers.remove(self)

    @staticmethod
    def modOrder(m):
        return m.order

    @classmethod
    def string(self):
        return self.text


class ChoiceReference(FSM, DependentObject):
    def __init__(self, widget, items):
        FSM.__init__(self, "")
        DependentObject.__init__(self, widget)

        self.changeSignal.connect(self.on_changed)
        widget.addItems(items)

    
    def on_changed(self,i):
        item = self.widget.currentText()
        item = item.replace(" ", "_")
        item = item.replace("-", "_")
        self.demand(item)
