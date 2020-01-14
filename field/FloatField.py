from PySide2.QtCore import Property
from PySide2.QtWidgets import QDoubleSpinBox, QSizePolicy

from field.Field import Field


class FloatField(Field):

    def __init__(self, property):
        super(FloatField, self).__init__(property)
        self._widget = QDoubleSpinBox()
        self._widget.valueChanged.connect(self.emitChanged)
        self._widget.setMinimum(property.min())
        self._widget.setMaximum(property.max())
        self._widget.setSingleStep(property.step())

    def value(self):
        return self._widget.value()

    def setValue(self, value):
        self._widget.setValue(value)

    def setReadOnly(self, value):
        self._widget.setReadOnly(value)

    valueProperty = Property(float, value, Field.setValueBlocked)  # C++: should be in parent class
