from PySide2.QtWidgets import QLineEdit, QDoubleSpinBox, QComboBox

from node.NodeType import NodeType


class PropertyWidgetFactory(object):

    def create(self, property):
        result = None
        type = property.type()
        if type == str:
            result = QLineEdit()
        elif type == float:
            result = QDoubleSpinBox()
        elif type == NodeType:
            result = QComboBox()
            result.addItems(NodeType.Names())
        return result

    def setReadOnly(self, index, property, widget):
        parent = index.parent()
        readOnly = property.readOnly() or not parent.isValid() # the top level nodes are read only
        type = property.type()
        if type == str or type == float:
            widget.setReadOnly(readOnly)
        elif type == NodeType:
            widget.setDisabled(readOnly)

    def mapToProperty(self, type):
        result = None
        if type == NodeType:
            result = 'currentIndex'
        return result
