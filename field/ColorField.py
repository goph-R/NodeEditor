from PySide2.QtCore import Property, Qt
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QPushButton, QColorDialog

from field.Field import Field


class ColorField(Field):

    def __init__(self, property):
        super(ColorField, self).__init__(property)
        self._readOnly = False
        self._color = None
        self._widget = QPushButton()
        self._widget.setFlat(True)
        self._widget.setCursor(Qt.PointingHandCursor)
        self._widget.setMinimumWidth(100)
        self._widget.clicked.connect(self.clicked)
        self.setValue(QColor('#fff'))

    def styleString(self, color):
        return 'QPushButton { background-color: ' + color + '; border-radius: 0; border: none }'

    def clicked(self):
        color = QColorDialog.getColor(self._color)
        if color.isValid():
            self.setValue(color)
            self.emitChanged()

    def value(self):
        return self._color

    def setValue(self, value):
        self._color = value
        self._widget.setStyleSheet(self.styleString(value.name()))

    def setReadOnly(self, value):
        self._readOnly = value

    valueProperty = Property(QColor, value, setValue)  # C++: should be in parent class

