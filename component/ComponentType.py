class ComponentType(object):  # C++: Q_ENUM

    General = 0
    Transform = 1
    Box = 2
    Sphere = 3
    PhongMaterial = 4

    @staticmethod
    def All():
        return [ComponentType.General, ComponentType.Transform, ComponentType.Box, ComponentType.Sphere, ComponentType.PhongMaterial]

    @staticmethod
    def Names():
        return ['General', 'Transform', 'Box', 'Sphere', 'PhongMaterial']
