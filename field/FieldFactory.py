from field.FloatField import FloatField
from field.StringField import StringField


class FieldFactory(object):

    def create(self, property):
        result = None
        type = property.type()
        if type == str:
            result = StringField(property)
        elif type == float:
            result = FloatField(property)
        result.init()
        return result

