from PySide2.QtCore import Qt
from PySide2.QtWidgets import QTreeWidget, QTreeWidgetItem, QDataWidgetMapper, QAbstractItemView

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

    def __init__(self):
        super(PropertyEditor, self).__init__()
        self._currentNodeType = None
        self._nodeTypeItem = None
        self._dataMapper = QDataWidgetMapper()
        self._widgetFactory = None
        self._nodeFactory = None
        self.setColumnCount(2)
        self.setHeaderLabels(['Name', 'Value'])
        self.setSelectionMode(QAbstractItemView.NoSelection)
        self.setAlternatingRowColors(True)
        self.setFocusPolicy(Qt.NoFocus)

    def setup(self, model, widgetFactory, nodeFactory):
        self._dataMapper.setModel(model)
        self._widgetFactory = widgetFactory
        self._nodeFactory = nodeFactory
        self._currentNodeType = None
        for index, property in enumerate(self._allProperties()):
            item = self._createItem(property)
            self._createWidget(item)

    def changeSelection(self, current, prev):
        node = current.internalPointer()
        nodeTypes = self._fetchNodeTypes(node)
        items = self._fetchVisibleItems(nodeTypes)
        self._setDataMapper(current, items)

    def _allProperties(self):
        result = []
        for type in NodeType.All():
            node = self._nodeFactory.create(type)
            for property in node.propertyMap():
                if property not in result:
                    result.append(property)
        return result

    def _fetchNodeTypes(self, node):
        result = set()
        for property in node.propertyMap():
            result.add(property.nodeType())
        return result

    def _fetchVisibleItems(self, nodeTypes):
        result = []
        for i in range(self.topLevelItemCount()):
            item = self.topLevelItem(i)
            if self._hideNodeType(item, nodeTypes):
                continue
            for index in range(item.childCount()):
                result.append(item.child(index))
        return result

    def _hideNodeType(self, item, nodeTypes):
        nodeType = item.data(0, Qt.UserRole)
        hide = nodeType not in nodeTypes
        item.setHidden(hide)
        return hide

    def _setDataMapper(self, current, items):
        self._dataMapper.clearMapping()
        for item in items:
            property = item.property()
            widget = self.itemWidget(item, 1)
            mapToProperty = self._widgetFactory.mapToProperty(property.type())
            if mapToProperty:
                self._dataMapper.addMapping(widget, property.column(), bytes(mapToProperty, 'ascii'))
            else:
                self._dataMapper.addMapping(widget, property.column())
        parent = current.parent()
        self._dataMapper.setRootIndex(parent)
        self._dataMapper.setCurrentModelIndex(current)

    def _createNodeTypeItem(self, nodeType):
        if self._currentNodeType == nodeType:
            return self._nodeTypeItem
        names = NodeType.Names()
        item = PropertyEditorItem()
        item.setText(0, names[nodeType])
        item.setData(0, Qt.UserRole, nodeType)
        self.addTopLevelItem(item)
        item.setExpanded(True)
        self._currentNodeType = nodeType
        self._nodeTypeItem = item
        return item

    def _createItem(self, property):
        parent = self._createNodeTypeItem(property.nodeType())
        item = PropertyEditorItem(parent)
        item.setText(0, property.label())
        item.setProperty(property)
        return item

    def _createWidget(self, item):
        widget = self._widgetFactory.create(item.property())
        self.setItemWidget(item, 1, widget)



