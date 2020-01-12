from component.Box import Box
from component.Component import Component
from component.Sphere import Sphere
from component.Translate import Translate
from node.Node import Node
from node.NodeType import NodeType


class NodeFactory(object):

    def create(self, type, name='', parent=None):
        general = Component()
        general.setName(name)
        result = Node(type, parent)
        result.addComponent(general)
        if type == NodeType.Sphere:
            result.addComponent(Translate())
            result.addComponent(Sphere())
        elif type == NodeType.Box:
            result.addComponent(Translate())
            result.addComponent(Box())
        result.init()
        return result



