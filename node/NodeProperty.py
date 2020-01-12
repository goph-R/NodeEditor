class NodeProperty(object):

    def __init__(self, label, name, type, readOnly=False):
        self._label = label
        self._name = name + 'Property'  # C++: 'Property' must be removed, this is only because of Python
        self._type = type  # C++: use a NodePropertyType Q_ENUM
        self._readOnly = readOnly
        self._nodeType = None
        self._column = None

    def __eq__(self, other):
        return isinstance(other, NodeProperty) \
               and self._label == other._label \
               and self._nodeType == other._nodeType

    def __ne__(self, other):
        return not isinstance(other, NodeProperty) \
               or self._label != other._label \
               or self._nodeType != other._nodeType

    def label(self):
        return self._label

    def type(self):
        return self._type

    def nodeType(self):
        return self._nodeType

    def setNodeType(self, value):
        self._nodeType = value

    def readOnly(self):
        return self._readOnly

    def column(self):
        return self._column

    def setColumn(self, value):
        self._column = value

    def name(self):
        return self._name