from PySide2.QtGui import QVector3D, QColor

from field.ColorField import ColorField
from field.FloatField import FloatField
from field.StringField import StringField
from field.Vector3Field import Vector3Field


class FieldFactory(object):

    def create(self, property):
        result = None
        type = property.type()

        if type == str:
            result = StringField(property)

        elif type == float:
            result = FloatField(property)

        elif type == QVector3D:
            result = Vector3Field(property)

        elif type == QColor:
            result = ColorField(property)

        result.init()
        return result

