from PyQt5 import QtCore, QtGui, QtWidgets
from copy import copy
class CheckableComboBox(QtWidgets.QComboBox):
    def __init__(self, parent=None):
        super(CheckableComboBox, self).__init__(parent)
        self._checkedItems = set()
        self.view().pressed.connect(self.handleItemPressed)
        self._changed = False

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        itemName = item.text()
        if item.checkState() == QtCore.Qt.Checked:
            item.setCheckState(QtCore.Qt.Unchecked)
            self._checkedItems -= set((item.text(),))
        else:
            item.setCheckState(QtCore.Qt.Checked)
            self._checkedItems |= set((item.text(),))
        self._changed = True

    def hidePopup(self):
        if not self._changed:
            super(CheckableComboBox, self).hidePopup()
        self._changed = False

    def itemChecked(self, index):
        item = self.model().item(index, self.modelColumn())
        return item.checkState() == QtCore.Qt.Checked

    def setItemChecked(self, index, checked):
        item = self.model().item(index, self.modelColumn())
        if checked:
            item.setCheckState(QtCore.Qt.Checked)
            self._checkedItems |= set((item.text(),))
        else:
            item.setCheckState(QtCore.Qt.Unchecked)
            self._checkedItems -= set((item.text(),))

    def setAllChecked(self,checked):
        if checked:state = QtCore.Qt.Checked
        else: state = QtCore.Qt.Unchecked
        for i in range(self.count()):
            item = self.model().item(i,self.modelColumn())
            item.setCheckState(state)

    def setItemWithNameChecked(self,name, checked):
        for i in range(self.count()):
            item = self.model().item(i, self.modelColumn())
            if item.text() == name:
                if checked:
                    item.setCheckState(QtCore.Qt.Checked)
                    self._checkedItems |= set((item.text(),))
                else:
                    item.setCheckState(QtCore.Qt.Unchecked)
                    self._checkedItems -= set((item.text(),))
                return
        raise NameError(name)

    def checkedItems(self):
        return copy(self._checkedItems)

    def clear(self):
        QtWidgets.QComboBox.clear(self)
        self._checkedItems.clear()
