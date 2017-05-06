from PyQt5 import QtCore, QtGui, QtWidgets

class ValueReference:
    # reference to a value stored within a qt widget
    def __init__(self, name, widget, valueconfig, default=None, format=None):
        self.name = name
        self.vconf = valueconfig
        self.widget = widget
        self.format = None
        self.modifiers = []
        if isinstance(widget, QtWidgets.QSpinBox):
            self._get = widget.value
            self._set = widget.setValue
            self._changeSignal = widget.valueChanged
            self._blockSignals = widget.blockSignals
            self._changeSignal.connect(self.on_changed)
        elif isinstance(widget, QtWidgets.QLabel) and not default is None:
            self._get = default
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
        #modifiers
        mstring = ""
        for mod in self.modifiers:
            mstring += mod.string()

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

    def applyMods(self, v):
        self.modifiers.sort(key=ValueModifier.modOrder)
        for mod in self.modifiers:
                v = mod.mod(v)
        return v


    def on_changed(self):
        # always called when value is changed by gui
        # uses ValueConfig to verify such a value is possible,
        # and either updates the fallback value, or resets to fallback
        value = self.get()
        if self.vconf.checkRequirements(value, self.lastValue):
            self.lastValue = value
        else:
            self.set(self.lastValue)

class DependantValueReference(ValueReference):
    # this value should not be set by UI
    def __init__(self, name, widget, valueconfig, default=None, format=None):
        assert(isinstance(widget, QtWidgets.QLabel))
        ValueReference.__init__(self,name,widget,valueconfig,default,format)
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
        else:
            valueref.modifiers.append(self)

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


