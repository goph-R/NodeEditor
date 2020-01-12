from property.Property import Property
from property.PropertyType import PropertyType
from node.Translate import Translate
from node.NodeType import NodeType


class Sphere(Translate):

    Radius = 5

    def createProperties(self):
        base = super(Sphere, self).createProperties()
        result = self.extendProperties(base, NodeType.Sphere, [
            Property('Radius', PropertyType.Float, 0.5)
        ])
        return result

    def type(self):
        return NodeType.Sphere

    def radius(self):
        return self.data(self.Radius)

    def setRadius(self, value):
        self.setData(self.Radius, value)
