from PySide2.Qt3DExtras import (Qt3DExtras)

from component.Component import Component
from component.ComponentType import ComponentType


class PhongMaterial(Component):

    def __init__(self):
        super(PhongMaterial, self).__init__()
        self._type = ComponentType.PhongMaterial
        self._component = Qt3DExtras.QPhongMaterial()
