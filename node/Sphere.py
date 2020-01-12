from PySide2.QtCore import Property

from node.NodeProperty import NodeProperty
from node.Translate import Translate
from node.NodeType import NodeType


class Sphere(Translate):

    def __init__(self, parent):
        super(Sphere, self).__init__(parent)
        self._type = NodeType.Sphere
        self._radius = 0.5

    def radius(self):
        return self._radius

    def setRadius(self, value):
        self._radius = value

    radiusProperty = Property(float, radius, setRadius)

    def createPropertyMap(self):
        base = super(Sphere, self).createPropertyMap()
        result = self.extendPropertyMap(base, NodeType.Sphere, [
            NodeProperty('Radius', 'radius', float)
        ])
        return result

