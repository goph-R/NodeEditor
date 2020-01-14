from PySide2.Qt3DCore import (Qt3DCore)
from PySide2.QtCore import Property

from component.Component import Component
from component.ComponentProperty import ComponentProperty
from component.ComponentType import ComponentType


class Translate(Component):

    def __init__(self):
        super(Translate, self).__init__()
        self._type = ComponentType.Translate
        self._component = Qt3DCore.QTransform()

    def x(self):
        return self._component.translation().x()

    def setX(self, value):
        v = self._component.translation()
        v.setX(value)
        self._component.setTranslation(v)

    def y(self):
        return self._component.translation().y()

    def setY(self, value):
        v = self._component.translation()
        v.setY(value)
        self._component.setTranslation(v)

    def z(self):
        return self._component.translation().z()

    def setZ(self, value):
        v = self._component.translation()
        v.setZ(value)
        self._component.setTranslation(v)

    xProperty = Property(float, x, setX)
    yProperty = Property(float, y, setY)
    zProperty = Property(float, z, setZ)

    def createPropertyMap(self):
        return [
            ComponentProperty('X', 'xProperty', float, True),
            ComponentProperty('Y', 'yProperty', float, True),
            ComponentProperty('Z', 'zProperty', float, True)
        ]
