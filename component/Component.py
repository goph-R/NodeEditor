from PySide2.QtCore import QObject, Property

from component.ComponentProperty import ComponentProperty


class Component(QObject):

    def __init__(self):
        super(Component, self).__init__()
        self._component = None
        self._type = None
        self._name = ''
        self._propertyMap = self.createPropertyMap()
        self._ownProperties = {}
        for property in self._propertyMap:
            self._ownProperties[property.name()] = property.own()
        self._node = None

    def setNode(self, value):  # C++: private method with friend class Node
        self._node = value

    def init(self):
        # in case it's needed, it will be called, when the node contains all of the components,
        # and the component has the _node value
        pass

    def addToEntity(self):
        return True if self._component else False

    def component(self):
        return self._component

    def type(self):
        return self._type

    def createPropertyMap(self):
        return {}

    def propertyMap(self):
        return self._propertyMap

    def property(self, name):
        if self._ownProperties[name]:
            return super(Component, self).property(name)
        else:
            return self._component.property(name)

    def setProperty(self, name, value):
        if self._ownProperties[name]:
            super(Component, self).setProperty(name, value)
        else:
            self._component.setProperty(name, value)

