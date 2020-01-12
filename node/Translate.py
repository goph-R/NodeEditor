from PySide2.QtCore import Property

from node.Node import Node
from node.NodeProperty import NodeProperty
from node.NodeType import NodeType


class Translate(Node):

    def __init__(self, parent):
        super(Translate, self).__init__(parent)
        self._x = 0
        self._y = 0
        self._z = 0

    def x(self):
        return self._x

    def setX(self, value):
        self._x = value

    def y(self):
        return self._y

    def setY(self, value):
        self._y = value

    def z(self):
        return self._z

    def setZ(self, value):
        self._z = value

    xProperty = Property(float, x, setX)
    yProperty = Property(float, y, setY)
    zProperty = Property(float, z, setZ)

    def createPropertyMap(self):
        base = super(Translate, self).createPropertyMap()
        result = self.extendPropertyMap(base, NodeType.Translate, [
            NodeProperty('X', 'x', float),
            NodeProperty('Y', 'y', float),
            NodeProperty('Z', 'z', float)
        ])
        return result
