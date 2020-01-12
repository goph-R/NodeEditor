from PySide2.QtCore import QObject


class Component(QObject):

    def __init__(self):
        super(Component, self).__init__()
        self._type = None
        self._name = ''
        self._propertyMap = self.createPropertyMap()
        self._node = None

    def setNode(self, value):  # C++: private method with friend class Node
        self._node = value

    def init(self):
        # in case it's needed, it will be called, when the node contains all of the components,
        # and the component has the _node value
        pass

    def type(self):
        return self._type

    def createPropertyMap(self):
        pass  # abstract

    def propertyMap(self):
        return self._propertyMap


