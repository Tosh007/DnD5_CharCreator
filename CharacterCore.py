from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from direct.fsm.FSM import FSM

class DependentObject(QObject):
    changeSignal = pyqtSignal()
    def __init__(self, widget):
        QObject.__init__(self, widget)
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
        v, mstring = self.applyMods(value,True)
        if (isinstance(self.widget, QtWidgets.QSpinBox)):
            self.widget.setSuffix(mstring)

class ValueConfig:
    @staticmethod
    def checkRequirements(value, oldvalue):
        return False

    getMaxValue = None


class ValueModifier:
    mod = lambda x: x
    order = 0
    text = "Null mod"

    @classmethod
    def connect(self, valueref):
        try:
            for ref in valueref:
                ref.modifiers.append(self)
                ref.changeSignal.emit()
        except TypeError:
            valueref.modifiers.append(self)
            valueref.changeSignal.emit()

    @classmethod
    def disconnect(self, valueref):
        try:
            for ref in valueref:
                ref.modifiers.remove(self)
                ref.changeSignal.emit()
        except TypeError:
            valueref.modifiers.remove(self)
            valueref.changeSignal.emit()

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
        widget.addItems(items)

    def on_changed(self):
        item = self.widget.currentText()
        item = item.replace(" ", "_")
        item = item.replace("-", "_")
        self.demand(item)
