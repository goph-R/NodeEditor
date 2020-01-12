class NodeType(object):  # C++: NodeType Q_ENUM

    General = 0
    Box = 1
    Sphere = 2

    @staticmethod
    def All():
        return [NodeType.General, NodeType.Box, NodeType.Sphere]

    def Names(self):
        return ['General', 'Box', 'Sphere']
