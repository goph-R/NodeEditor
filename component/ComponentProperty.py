class ComponentProperty(object):

    def __init__(self, label, name, type, own=False, readOnly=False, min=-100000, max=100000, step=1):
        self._name = name
        self._own = own
        self._label = label
        self._type = type  # C++: use a ComponentPropertyType Q_ENUM
        self._readOnly = readOnly
        self._min = min
        self._max = max
        self._column = None
        self._step = step

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

    def min(self):
        return self._min

    def max(self):
        return self._max

    def step(self):
        return self._step
