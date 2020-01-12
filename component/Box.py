from PySide2.QtCore import Property

from component.Component import Component
from component.ComponentProperty import ComponentProperty
from component.ComponentType import ComponentType


class Box(Component):

    def __init__(self):
        super(Box, self).__init__()
        self._type = ComponentType.Box
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
        return [
            ComponentProperty('Width', 'width', float),
            ComponentProperty('Height', 'height', float),
            ComponentProperty('Depth', 'depth', float)
        ]
