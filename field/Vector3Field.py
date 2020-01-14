from PySide2.QtCore import Property
from PySide2.QtGui import QVector3D
from PySide2.QtWidgets import QDoubleSpinBox, QWidget, QHBoxLayout, QLabel

from field.Field import Field


class Vector3Field(Field):

    def __init__(self, property):
        super(Vector3Field, self).__init__(property)
        self._value = QVector3D()
        self._widget = QWidget()
        self._widgets = [None, None, None]
        l = QHBoxLayout(self._widget)
        l.setContentsMargins(0, 0, 0, 0)
        for i in range(3):
            self._widgets[i] = QDoubleSpinBox()
            self._widgets[i].valueChanged.connect(self.emitChanged)
            self._widgets[i].setMinimum(property.min())
            self._widgets[i].setMaximum(property.max())
            self._widgets[i].setSingleStep(property.step())
            l.addWidget(self._widgets[i])

    def value(self):
        return QVector3D(self._widgets[0].value(), self._widgets[1].value(), self._widgets[2].value())

    def setValue(self, value):
        for i in range(3):
            self._widgets[i].blockSignals(True)
        self._widgets[0].setValue(value.x())
        self._widgets[1].setValue(value.y())
        self._widgets[2].setValue(value.z())
        for i in range(3):
            self._widgets[i].blockSignals(False)

    def setReadOnly(self, value):
        for i in range(3):
            self._widgets[i].setReadOnly(value)

    valueProperty = Property(QVector3D, value, setValue)  # C++: should be in parent class
