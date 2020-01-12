class NodeType(object):  # C++: NodeType Q_ENUM

    General = 0
    Box = 1
    Sphere = 2

    @staticmethod
    def All():
        return [NodeType.General, NodeType.Box, NodeType.Sphere]

    @staticmethod
    def Names():
        return ['General', 'Box', 'Sphere']
