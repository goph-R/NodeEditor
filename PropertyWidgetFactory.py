from PySide2.QtWidgets import QLineEdit, QDoubleSpinBox, QComboBox

from node.NodeType import NodeType


class PropertyWidgetFactory(object):

    def create(self, property):
        result = None
        type = property.type()
        readOnly = property.readOnly()
        if type == str:
            result = QLineEdit()
            result.setReadOnly(readOnly)
        elif type == float:
            result = QDoubleSpinBox()
            result.setReadOnly(readOnly)
        elif type == NodeType:
            result = QComboBox()
            result.addItems(NodeType.Names())
            result.setDisabled(readOnly)
        return result

    def mapToProperty(self, type):
        result = None
        if type == NodeType:
            result = 'currentIndex'
        return result
