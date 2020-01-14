from field.FloatField import FloatField
from field.StringField import StringField


class FieldFactory(object):

    def create(self, type):
        result = None
        if type == str:
            result = StringField()
        elif type == float:
            result = FloatField()
        result.init()
        return result

