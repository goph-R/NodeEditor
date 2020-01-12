from property.Property import Property
from property.PropertyType import PropertyType
from node.Translate import Translate
from node.NodeType import NodeType


class Box(Translate):

    Width = 5
    Height = 6
    Depth = 7

    def createProperties(self):
        base = super(Box, self).createProperties()
        result = self.extendProperties(base, NodeType.Box, [
            Property('Width', PropertyType.Float, 1),
            Property('Height', PropertyType.Float, 1),
            Property('Depth', PropertyType.Float, 1)
        ])
        return result

    def type(self):
        return NodeType.Box

    def width(self):
        return self.data(self.Width)

    def setWidth(self, value):
        self.setData(self.Width, value)

    def height(self):
        return self.data(self.Height)

    def setHeight(self, value):
        self.setData(self.Height, value)

    def depth(self):
        return self.data(self.Depth)

    def setDepth(self, value):
        self.setData(self.Depth, value)