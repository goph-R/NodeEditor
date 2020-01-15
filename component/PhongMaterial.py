from PySide2.Qt3DExtras import (Qt3DExtras)
from PySide2.QtGui import QColor

from component.Component import Component
from component.ComponentProperty import ComponentProperty
from component.ComponentType import ComponentType


class PhongMaterial(Component):

    def __init__(self):
        super(PhongMaterial, self).__init__()
        self._type = ComponentType.PhongMaterial
        self._component = Qt3DExtras.QPhongMaterial()

    def createPropertyMap(self):
        return [
            ComponentProperty('Ambient', 'ambient', QColor),
            ComponentProperty('Diffuse', 'diffuse', QColor),
            ComponentProperty('Specular', 'specular', QColor),
            ComponentProperty('Shininess', 'shininess', float, min=0, max=1000, step=10),
        ]