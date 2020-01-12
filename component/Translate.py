from PySide2.QtCore import Property

from component.Component import Component
from component.ComponentProperty import ComponentProperty
from component.ComponentType import ComponentType


class Translate(Component):

    def __init__(self):
        super(Translate, self).__init__()
        self._type = ComponentType.Translate
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
        return [
            ComponentProperty('X', 'x', float),
            ComponentProperty('Y', 'y', float),
            ComponentProperty('Z', 'z', float)
        ]
