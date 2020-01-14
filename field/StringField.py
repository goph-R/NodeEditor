from PySide2.QtCore import Property
from PySide2.QtWidgets import QLineEdit

from field.Field import Field


class StringField(Field):

    def __init__(self, property):
        super(StringField, self).__init__(property)
        self._widget = QLineEdit()
        self._widget.textChanged.connect(self.emitChanged)

    def value(self):
        return self._widget.text()

    def setValue(self, value):
        self._widget.setText(value)

    def setReadOnly(self, value):
        self._widget.setReadOnly(value)

    valueProperty = Property(str, value, Field.setValueBlocked)  # C++: should be in parent class

