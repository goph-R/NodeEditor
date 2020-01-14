from PySide2.Qt3DCore import (Qt3DCore)
from PySide2.QtCore import Property
from PySide2.QtGui import QVector3D

from component.Component import Component
from component.ComponentProperty import ComponentProperty
from component.ComponentType import ComponentType


class Transform(Component):

    def __init__(self):
        super(Transform, self).__init__()
        self._type = ComponentType.Transform
        self._component = Qt3DCore.QTransform()

    def eulerRotation(self):
        return QVector3D(
            self._component.rotationX(),
            self._component.rotationY(),
            self._component.rotationZ()
        )

    def setEulerRotation(self, value):
        self._component.setRotationX(value.x())
        self._component.setRotationY(value.y())
        self._component.setRotationZ(value.z())

    eulerRotationProperty = Property(QVector3D, eulerRotation, setEulerRotation)

    def createPropertyMap(self):
        return [
            ComponentProperty('Translation', 'translation', QVector3D),
            ComponentProperty('Rotation', 'eulerRotationProperty', QVector3D, True, step=10),
            ComponentProperty('Scale', 'scale3D', QVector3D, min=0, step=0.1)
        ]
