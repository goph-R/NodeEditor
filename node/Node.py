from PySide2.QtCore import QObject, Property

from node.NodeProperty import NodeProperty
from node.NodeType import NodeType


class Node(QObject):  # need to extend QObject because of the properties

    def __init__(self, parent):
        super(Node, self).__init__(parent)
        self._children = []  # C++: QList<Node*>
        self._parent = parent
        self._name = ''
        self._type = NodeType.General
        self._propertyMap = self.createPropertyMap()  # C++: QList<NodeProperty*>
        self.setPropertyColumns()
        if parent is not None:
            parent.addChild(self)

    def name(self):
        return self._name

    def setName(self, value):
        self._name = value

    def type(self):
        return self._type

    nameProperty = Property(str, name, setName)  # C++: Q_PROPERTY(QString name READ name WRITE setName)
    typeProperty = Property(int, type)           # C++: Q_PROPERTY(int type READ type WRITE setType)

    def createPropertyMap(self):
        base = [
            NodeProperty('Name', 'name', str),  # C++: we have to use a NodePropertyType, can't pass type as an argument
            NodeProperty('Type', 'type', NodeType, True)
        ]
        self.setNodeType(NodeType.General, base)
        return base

    def extendPropertyMap(self, base, nodeType, result):
        self.setNodeType(nodeType, result)
        base.extend(result)  # C++: QList::append(QList)
        return base

    def setNodeType(self, nodeType, properties):
        for column, property in enumerate(properties):  # C++: for (int column = 0; column < properties.count(); i++) {
            property.setNodeType(nodeType)              #          auto property = properties.at(column);
                                                        #          property->setNodeType(nodeType);
                                                        #      }

    def setPropertyColumns(self):
        for column, property in enumerate(self._propertyMap):
            property.setColumn(column)

    def propertyMap(self):
        return self._propertyMap

    def addChild(self, child):
        self._children.append(child)

    def childCount(self):
        return len(self._children)

    def child(self, row):
        return self._children[row]

    def row(self):
        if self._parent is not None:
            return self._parent._children.index(self)

    def parent(self):
        return self._parent

    def setParent(self, value):
        self._parent = value

    def insertChild(self, position, child):
        self._children.insert(position, child)

    def removeChild(self, position):
        self._children.remove(self._children[position])

    def data(self, column):
        name = self._propertyMap[column].name()
        return self.property(name)

    def setData(self, column, value):
        name = self._propertyMap[column].name()
        self.setProperty(name, value)
