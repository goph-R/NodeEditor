from PySide2.QtCore import QObject, Property

from component.ComponentProperty import ComponentProperty
from component.ComponentType import ComponentType


class Component(QObject):

    def __init__(self):
        super(Component, self).__init__()
        self._type = ComponentType.General
        self._name = ''
        self._propertyMap = self.createPropertyMap()
        self._node = None

    def setNode(self, value):
        self._node = value

    def init(self):
        # in case it's needed, it will be called, when the node contains all of the components,
        # and the component has the _node value
        pass

    def type(self):
        return self._type

    def name(self):
        return self._name

    def setName(self, value):
        self._name = value

    nameProperty = Property(str, name, setName)  # C++: Q_PROPERTY(QString name READ name WRITE setName)

    def createPropertyMap(self):
        return [
            ComponentProperty('Name', 'name', str),  # C++: we have to use a NodePropertyType, can't pass type as an argument
        ]

    def propertyMap(self):
        return self._propertyMap


