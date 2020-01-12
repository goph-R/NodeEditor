from PySide2.QtWidgets import QLineEdit, QDoubleSpinBox, QComboBox

from property.PropertyType import PropertyType
from node.NodeType import NodeType


class PropertyWidgetFactory(object):

    def create(self, property):
        result = None
        type = property.type()
        readOnly = property.readOnly()
        if type == PropertyType.String:
            result = QLineEdit()
            result.setReadOnly(readOnly)
        elif type == PropertyType.Float:
            result = QDoubleSpinBox()
            result.setReadOnly(readOnly)
        elif type == PropertyType.NodeType:
            result = QComboBox()
            result.addItems(NodeType.Names())
            result.setDisabled(readOnly)
        return result

    def mapToProperty(self, type):
        result = None
        if type == PropertyType.NodeType:
            result = 'currentIndex'
        return result
