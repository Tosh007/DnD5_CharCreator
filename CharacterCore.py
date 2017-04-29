from PyQt5 import QtCore, QtGui, QtWidgets

class ValueReference:
    # reference to a value stored within a qt widget
    def __init__(self, name, widget, valueconfig):
        self.name = name
        self.vconf = valueconfig
        self.widget = widget
        if isinstance(widget, QtWidgets.QSpinBox):
            self._get = widget.value
            self._set = widget.setValue
            self._changeSignal = widget.valueChanged
            self._blockSignals = widget.blockSignals
        else:
            raise NotImplemented("only QSpinBox supported")
        self._changeSignal.connect(self.on_changed)
        self.lastValue = self.get()

    def set(self, value):
        self._blockSignals(True)
        self._set(value)
        self._blockSignals(False)

    def get(self):
        # returns current value from qt widget
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


class ValueConfig:    
    def checkRequirements(value, oldvalue):
        return True



class ValueModifier:pass

