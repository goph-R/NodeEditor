from PySide2.QtCore import Property

from node.NodeProperty import NodeProperty
from node.Translate import Translate
from node.NodeType import NodeType


class Box(Translate):

    def __init__(self, parent):
        super(Box, self).__init__(parent)
        self._type = NodeType.Box
        self._width = 1
        self._height = 1
        self._depth = 1

    def getWidth(self):
        return self._width

    def setWidth(self, value):
        self._width = value

    def getHeight(self):
        return self._height

    def setHeight(self, value):
        self._height = value

    def getDepth(self):
        return self._depth

    def setDepth(self, value):
        self._depth = value

    width = Property(float, getWidth, setHeight)
    height = Property(float, getHeight, setHeight)
    depth = Property(float, getDepth, setDepth)

    def createPropertyMap(self):
        base = super(Box, self).createPropertyMap()
        result = self.extendPropertyMap(base, NodeType.Box, [
            NodeProperty('Width', 'width', float),
            NodeProperty('Height', 'height', float),
            NodeProperty('Depth', 'depth', float)
        ])
        return result
