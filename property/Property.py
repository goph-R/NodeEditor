class Property(object):

    def __init__(self, name, type, defaultValue=None, readOnly=False):
        self._name = name
        self._type = type
        self._readOnly = readOnly
        self._defaultValue = defaultValue
        # set these later
        self._group = None
        self._column = -1

    def __eq__(self, other):
        return isinstance(other, Property) \
            and self._name == other._name \
            and self._group == other._group

    def __ne__(self, other):
        return not isinstance(other, Property) \
            or self._name != other._name \
            or self._group != other._group

    def name(self):
        return self._name

    def type(self):
        return self._type

    def group(self):
        return self._group

    def setGroup(self, value):
        self._group = value

    def readOnly(self):
        return self._readOnly

    def column(self):
        return self._column

    def setColumn(self, value):
        self._column = value

    def defaultValue(self):
        return self._defaultValue






