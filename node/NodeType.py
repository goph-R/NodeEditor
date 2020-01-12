class NodeType(object):

    General = 0
    Translate = 1
    Box = 2
    Sphere = 3

    @staticmethod
    def All():
        return [NodeType.General, NodeType.Translate, NodeType.Box, NodeType.Sphere]

    @staticmethod
    def Names():
        return ['General', 'Translate', 'Box', 'Sphere']
