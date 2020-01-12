from property.Property import Property
from property.PropertyType import PropertyType
from node.Node import Node
from node.NodeType import NodeType


class Translate(Node):

    X = 2
    Y = 3
    Z = 4

    def createProperties(self):
        base = super(Translate, self).createProperties()
        result = self.extendProperties(base, NodeType.Translate, [
            Property('X', PropertyType.Float, 0),
            Property('Y', PropertyType.Float, 0),
            Property('Z', PropertyType.Float, 0)
        ])
        return result

    def type(self):
        return NodeType.Translate

    def x(self):
        return self.data(self.X)

    def setX(self, value):
        self.setData(self.X, value)

    def y(self):
        return self.data(self.Y)

    def setY(self, value):
        self.setData(self.Y, value)

    def z(self):
        return self.data(self.Z)

    def setZ(self, value):
        self.setData(self.Z, value)
