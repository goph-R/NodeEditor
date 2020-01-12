class Node(object):

    def __init__(self, type, parent):
        super(Node, self).__init__()
        self._type = type
        self._parent = parent
        self._children = []  # C++: QList<Node*>
        self._components = {}  # C++: QHash<ComponentType, Component*>
        self._propertyMap = []  # C++: QList<NodeProperty*>
        self._componentMap = []  # C++: QList<Component*>
        if parent is not None:
            parent.addChild(self)

    def type(self):
        return self._type

    def addComponent(self, component):
        self._components[component.type()] = component

    def hasComponent(self, type):
        return type in self._components

    def component(self, type):
        return self._components[type] if self.hasComponent(type) else None

    def components(self):
        return self._components

    def propertyMap(self):
        return self._propertyMap

    def init(self):
        column = 0
        for component in self._components.values():
            component.setNode(self)
            properties = component.propertyMap()
            self._propertyMap.extend(properties)
            for property in properties:
                property.setColumn(column)
                self._componentMap.append(component)
                column += 1
        for component in self._components.values():
            component.init()


    def addChild(self, child):
        self._children.append(child)

    def childCount(self):
        return len(self._children)

    def child(self, row):
        return self._children[row]

    def row(self):
        if self._parent is not None:
            return self._parent._children.index(self)

    def parent(self):
        return self._parent

    def setParent(self, value):
        self._parent = value

    def insertChild(self, position, child):
        self._children.insert(position, child)

    def removeChild(self, position):
        self._children.remove(self._children[position])

    def data(self, column):
        name = self._propertyMap[column].name()
        component = self._componentMap[column]
        return component.property(name)

    def setData(self, column, value):  # C++: the value is a QVariant
        name = self._propertyMap[column].name()
        component = self._componentMap[column]
        component.setProperty(name, value)
