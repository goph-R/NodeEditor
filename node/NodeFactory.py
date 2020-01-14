from component.Box import Box
from component.General import General
from component.PhongMaterial import PhongMaterial
from component.Sphere import Sphere
from component.Transform import Transform
from node.Node import Node
from node.NodeType import NodeType


class NodeFactory(object):

    def create(self, type, name='', parent=None):
        result = Node(type, parent)

        general = General()
        general.setName(name)
        result.addComponent(general)

        if type == NodeType.Sphere:
            result.addComponent(Transform())
            result.addComponent(Sphere())
            result.addComponent(PhongMaterial())

        result.init()
        return result



