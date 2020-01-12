from node.NodeType import NodeType
from node.Node import Node
from node.Box import Box
from node.Sphere import Sphere
from node.Translate import Translate


class NodeFactory(object):

    def create(self, type, name='', parent=None):
        result = None
        if type == NodeType.General:
            result = Node(parent)
        elif type == NodeType.Translate:
            result = Translate(parent)
        elif type == NodeType.Box:
            result = Box(parent)
        elif type == NodeType.Sphere:
            result = Sphere(parent)
        result.setName(name)
        return result



