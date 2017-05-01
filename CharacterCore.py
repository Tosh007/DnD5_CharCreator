from PyQt5 import QtCore, QtGui, QtWidgets

class ValueReference:
    # reference to a value stored within a qt widget
    def __init__(self, name, widget, valueconfig, default=None, format=None):
        self.name = name
        self.vconf = valueconfig
        self.widget = widget
        self.format = None
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
        

    def get(self):
        # returns current value from qt widget
        if isinstance(self._get, str):
            return int(self._get)
        elif isinstance(self._get, int):
            return self._get
        else: 
            return self._get()

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



class ValueModifier:pass

