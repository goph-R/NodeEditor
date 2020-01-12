from PySide2.QtCore import Qt
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

    def __init__(self):
        super(PropertyEditor, self).__init__()
        self._dataMapper = QDataWidgetMapper()
        self._currentComponentType = None
        self._widgetFactory = None
        self._nodeFactory = None
        # setup ui
        self.setColumnCount(2)
        self.setHeaderLabels(['Name', 'Value'])
        self.setSelectionMode(QAbstractItemView.NoSelection)
        self.setAlternatingRowColors(True)
        self.setFocusPolicy(Qt.NoFocus)

    def init(self, model, widgetFactory, nodeFactory):
        self._dataMapper.setModel(model)
        self._widgetFactory = widgetFactory
        self._nodeFactory = nodeFactory
        self._createAllItems()

    def _createAllItems(self):
        for componentType, properties in self._allProperties().items():
            topItem = self._createComponentItem(componentType)
            for property in properties:
                item = PropertyEditorItem(topItem)
                item.setText(0, property.label())
                widget = self._widgetFactory.create(property)
                self.setItemWidget(item, 1, widget)

    def _allProperties(self):
        result = {}
        for type in NodeType.All():
            node = self._nodeFactory.create(type)
            for component in node.components().values():
                result[component.type()] = component.propertyMap()
        return result

    def changeSelection(self, current, prev):
        node = current.internalPointer()
        visibleItems = self._fetchVisibleItems(node)
        self._setDataMapper(current, visibleItems)

    def _fetchVisibleItems(self, node):
        result = []
        for i in range(self.topLevelItemCount()):
            componentItem = self.topLevelItem(i)
            componentType = componentItem.data(0, Qt.UserRole)
            component = node.component(componentType)
            if component is None:
                componentItem.setHidden(True)
                continue
            componentItem.setHidden(False)
            for column, property in enumerate(component.propertyMap()):
                item = componentItem.child(column)
                item.setProperty(property)
                result.append(item)
        return result

    def _setDataMapper(self, current, items):
        self._dataMapper.clearMapping()
        for item in items:
            property = item.property()
            widget = self.itemWidget(item, 1)
            self._widgetFactory.setReadOnly(current, property, widget)
            mapToProperty = self._widgetFactory.mapToProperty(property.type())
            if mapToProperty:
                self._dataMapper.addMapping(widget, property.column(), bytes(mapToProperty, 'ascii'))
            else:
                self._dataMapper.addMapping(widget, property.column())
        parent = current.parent()
        self._dataMapper.setRootIndex(parent)
        self._dataMapper.setCurrentModelIndex(current)

    def _createComponentItem(self, type):
        names = ComponentType.Names()
        item = PropertyEditorItem()
        item.setText(0, names[type])
        item.setData(0, Qt.UserRole, type)
        self.addTopLevelItem(item)
        item.setExpanded(True)
        return item
