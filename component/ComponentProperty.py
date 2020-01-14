class ComponentProperty(object):

    def __init__(self, label, name, type, own=False, readOnly=False):
        self._name = name
        self._own = own
        self._label = label
        self._type = type  # C++: use a ComponentPropertyType Q_ENUM
        self._readOnly = readOnly
        self._column = None

    def own(self):
        return self._own

    def label(self):
        return self._label

    def type(self):
        return self._type

    def readOnly(self):
        return self._readOnly

    def column(self):
        return self._column

    def setColumn(self, value):
        self._column = value

    def name(self):
        return self._name