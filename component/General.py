from PySide2.QtCore import QObject, Property

from component.Component import Component
from component.ComponentProperty import ComponentProperty
from component.ComponentType import ComponentType


class General(Component):

    def __init__(self):
        super(General, self).__init__()
        self._type = ComponentType.General
        self._name = ''
        self._propertyMap = self.createPropertyMap()

    def name(self):
        return self._name

    def setName(self, value):
        self._name = value

    nameProperty = Property(str, name, setName)  # C++: Q_PROPERTY(QString name READ name WRITE setName)

    def createPropertyMap(self):
        return [
            ComponentProperty('Name', 'name', str),  # C++: we have to use a ComponentPropertyType, can't pass type as an argument
        ]
