from property.Property import Property
from property.PropertyType import PropertyType
from node.NodeType import NodeType


class Node(object):

    Name = 0
    Type = 1

    def __init__(self, parent):
        self._children = []
        self._parent = parent
        self._properties = self.createAllProperties()
        self._values = [0 for i in range(len(self._properties))]
        self.setDefaultValues()
        if parent is not None:
            parent.addChild(self)

    def name(self):
        return self.data(self.Name)

    def setName(self, value):
        self.setData(self.Name, value)

    def type(self):
        return NodeType.General

    def createProperties(self):
        base = [
            Property('Name', PropertyType.String, ''),
            Property('Type', PropertyType.NodeType, self.type(), True)
        ]
        self.setPropertiesGroup(base, NodeType.General)
        return base

    def extendProperties(self, base, type, properties):
        self.setPropertiesGroup(properties, type)
        base.extend(properties)
        return base

    def createAllProperties(self):
        result = self.createProperties()
        for column, property in enumerate(result):
            property.setColumn(column)
        return result

    def setDefaultValues(self):
        for column, property in enumerate(self.properties()):
            self.setData(column, property.defaultValue())

    def setPropertiesGroup(self, properties, group):
        for property in properties:
            property.setGroup(group)

    def properties(self):
        return self._properties

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
        return self._values[column]

    def setData(self, column, value):
        self._values[column] = value