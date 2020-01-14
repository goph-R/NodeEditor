from PySide2.QtCore import Signal, Property
from PySide2.QtWidgets import QWidget, QSizePolicy, QHBoxLayout


class Field(QWidget):

    changed = Signal()

    def __init__(self, property):
        super(Field, self).__init__()
        self._widget = None
        self._layout = QHBoxLayout(self)  # without this the child widget will not be expanded
        self._layout.setContentsMargins(0, 0, 0, 0)

    def init(self):
        self._layout.addWidget(self._widget)

    def emitChanged(self):
        self.changed.emit()

    def value(self):
        pass  # abstract

    def setValueBlocked(self, value):  # we don't want to emit, when the data mapper sets the property
        self._widget.blockSignals(True)
        self.setValue(value)
        self._widget.blockSignals(False)

    def setValue(self, value):
        pass  # abstract

    def setReadOnly(self, value):
        pass  # abstract

    # C++: we should put the property here with QVariant type, but we can't use that type in PySide
