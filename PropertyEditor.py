from PySide2.QtCore import Qt, QMetaObject
from PySide2.QtWidgets import QTreeWidget, QTreeWidgetItem, QDataWidgetMapper, QAbstractItemView

from component.ComponentType import ComponentType
from node.NodeType import NodeType


class PropertyEditorItem(QTreeWidgetItem):

    def __init__(self, parent=None):
        super(PropertyEditorItem, self).__init__(parent)
        self._property = None

    def property(self):
        return self._property

    def setProperty(self, value):
        self._property = value


class PropertyEditor(QTreeWidget):

    def __init__(self, model, nodeFactory, fieldFactory):
        super(PropertyEditor, self).__init__()
        self._dataMapper = QDataWidgetMapper()
        self._dataMapper.setModel(model)
        self._dataMapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self._model = model
        self._currentIndex = None
        self._fieldFactory = fieldFactory
        self._nodeFactory = nodeFactory
        # setup ui
        self.setColumnCount(2)
        self.setHeaderLabels(['Name', 'Value'])
        self.setSelectionMode(QAbstractItemView.NoSelection)
        self.setAlternatingRowColors(True)
        self.setFocusPolicy(Qt.NoFocus)
        # create all items per component
        self._createAllItems()
        self.resizeColumnToContents(0)
        self.setColumnWidth(0, self.columnWidth(0) + 20)

    def _createAllItems(self):
        for type, properties in self._allProperties().items():
            topItem = self._createComponentItem(type)
            if type == ComponentType.General:
               self._createNodeTypeItem(topItem)
            for property in properties:
                item = PropertyEditorItem(topItem)
                item.setText(0, property.label())
                field = self._fieldFactory.create(property)
                self.setItemWidget(item, 1, field)

    def _allProperties(self):
        result = {}
        for type in NodeType.All():
            node = self._nodeFactory.create(type)
            for component in node.components().values():
                result[component.type()] = component.propertyMap()
        return result

    def _createComponentItem(self, type):
        names = ComponentType.Names()
        item = PropertyEditorItem()
        item.setText(0, names[type])
        item.setData(0, Qt.UserRole, type)
        self.addTopLevelItem(item)
        item.setExpanded(True)
        return item

    def _createNodeTypeItem(self, topItem):
        self._nodeTypeItem = PropertyEditorItem(topItem)
        self._nodeTypeItem.setText(0, 'Type')
        font = self._nodeTypeItem.font(1)  # don't ask, this is how it will be the same size as in the editors
        font.setPointSize(font.pointSize())
        self._nodeTypeItem.setFont(1, font)

    def changeSelection(self, current, prev):
        node = current.internalPointer()
        self._currentIndex = current
        items = self._itemsForNode(node)
        self._setMapping(current, items)

    def _itemsForNode(self, node):
        result = []
        names = NodeType.Names()
        self._nodeTypeItem.setText(1, names[node.type()])
        for i in range(self.topLevelItemCount()):
            item = self.topLevelItem(i)
            type = item.data(0, Qt.UserRole)
            component = node.component(type)
            item.setHidden(not component)
            if component is None:
                continue
            result.extend(self._itemsForComponent(component, item))
        return result

    def _itemsForComponent(self, component, parentItem):
        result = []
        for column, property in enumerate(component.propertyMap()):
            offset = 1 if component.type() == ComponentType.General else 0  # the first item of General is Type
            item = parentItem.child(column + offset)
            item.setProperty(property)
            result.append(item)
        return result

    def _setMapping(self, current, items):
        self._dataMapper.clearMapping()
        fields = []
        for item in items:
            fields.append(self._mapField(current, item))
        parent = current.parent()
        self._dataMapper.setRootIndex(parent)
        self._dataMapper.setCurrentModelIndex(current)
        for field in fields:
            field.changed.connect(self._dataMapper.submit)  # this MUST be after the setCurrentModelIndex

    def _mapField(self, current, item):
        property = item.property()
        if not property:  # General/Type doesn't have a property
           return
        field = self.itemWidget(item, 1)
        parent = current.parent()
        readOnly = property.readOnly() or not parent.isValid()  # the top level nodes are read only
        field.setReadOnly(readOnly)
        self._dataMapper.addMapping(field, property.column(), b'valueProperty')
        return field




