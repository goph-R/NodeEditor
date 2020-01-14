from PySide2.Qt3DCore import (Qt3DCore)
from PySide2.QtGui import QVector3D

from component.Component import Component
from component.ComponentProperty import ComponentProperty
from component.ComponentType import ComponentType


class Transform(Component):

    def __init__(self):
        super(Transform, self).__init__()
        self._type = ComponentType.Transform
        self._component = Qt3DCore.QTransform()

    def createPropertyMap(self):
        return [
            ComponentProperty('Translation', 'translation', QVector3D)
        ]
