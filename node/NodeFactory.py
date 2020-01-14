from component.Box import Box
from component.General import General
from component.PhongMaterial import PhongMaterial
from component.Sphere import Sphere
from component.Translate import Translate
from node.Node import Node
from node.NodeType import NodeType


class NodeFactory(object):

    def create(self, type, name='', parent=None):
        general = General()
        general.setName(name)
        result = Node(type, parent)
        result.addComponent(general)
        if type == NodeType.Sphere:
            result.addComponent(Translate())
            result.addComponent(Sphere())
            result.addComponent(PhongMaterial())
        # elif type == NodeType.Box:
        #     result.addComponent(Translate())
        #     result.addComponent(Box())
        result.init()
        return result



