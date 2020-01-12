from PySide2.QtCore import Property

from component.Component import Component
from component.ComponentProperty import ComponentProperty
from component.ComponentType import ComponentType


class Sphere(Component):

    def __init__(self):
        super(Sphere, self).__init__()
        self._type = ComponentType.Sphere
        self._radius = 0.5

    def radius(self):
        return self._radius

    def setRadius(self, value):
        self._radius = value

    radiusProperty = Property(float, radius, setRadius)

    def createPropertyMap(self):
        return [
            ComponentProperty('Radius', 'radius', float)
        ]
