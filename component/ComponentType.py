class ComponentType(object):  # C++: Q_ENUM

    General = 0
    Translate = 1
    Box = 2
    Sphere = 3
    PhongMaterial = 4

    @staticmethod
    def All():
        return [ComponentType.General, ComponentType.Translate, ComponentType.Box, ComponentType.Sphere, ComponentType.PhongMaterial]

    @staticmethod
    def Names():
        return ['General', 'Translate', 'Box', 'Sphere', 'PhongMaterial']
