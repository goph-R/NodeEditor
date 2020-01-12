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

    def width(self):
        return self._width

    def setWidth(self, value):
        self._width = value

    def height(self):
        return self._height

    def setHeight(self, value):
        self._height = value

    def depth(self):
        return self._depth

    def setDepth(self, value):
        self._depth = value

    widthProperty = Property(float, width, setHeight)
    heightProperty = Property(float, height, setHeight)
    depthProperty = Property(float, depth, setDepth)

    def createPropertyMap(self):
        base = super(Box, self).createPropertyMap()
        result = self.extendPropertyMap(base, NodeType.Box, [
            NodeProperty('Width', 'width', float),
            NodeProperty('Height', 'height', float),
            NodeProperty('Depth', 'depth', float)
        ])
        return result
