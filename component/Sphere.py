from PySide2.QtCore import Property
from PySide2.Qt3DExtras import (Qt3DExtras)

from component.Component import Component
from component.ComponentProperty import ComponentProperty
from component.ComponentType import ComponentType


class Sphere(Component):

    def __init__(self):
        super(Sphere, self).__init__()
        self._type = ComponentType.Sphere
        self._component = Qt3DExtras.QSphereMesh()
        self._component.setRadius(5)

    def createPropertyMap(self):
        return [
            ComponentProperty('Radius', 'radius', float)
        ]
