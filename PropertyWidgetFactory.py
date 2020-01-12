from PySide2.QtWidgets import QLineEdit, QDoubleSpinBox, QComboBox


class PropertyWidgetFactory(object):

    def create(self, property):
        result = None
        type = property.type()
        if type == str:
            result = QLineEdit()
        elif type == float:
            result = QDoubleSpinBox()
        #
        # just an example for a custom widget
        #
        # elif type == ComponentType:
        #     result = QComboBox()
        #     result.addItems(ComponentType.Names())
        return result

    def setReadOnly(self, index, property, widget):
        parent = index.parent()
        readOnly = property.readOnly() or not parent.isValid() # the top level nodes are read only
        type = property.type()
        if type == str or type == float:
            widget.setReadOnly(readOnly)
        #
        # just an example for a custom widget
        #
        # elif type == ComponentType:
        #     widget.setDisabled(readOnly)

    def mapToProperty(self, type):
        result = None
        #
        # just an example for a custom widget
        #
        # if type == ComponentType:
        #     result = 'currentIndex'
        return result
