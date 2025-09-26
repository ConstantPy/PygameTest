class Entity:
    def __init__(self, *components, x=0, y=0):
        self.components = []
        self.x = x
        self.y = y
        for component in components:
            self.add(component)

    def add(self, component):
        component.entity = self
        self.components.append(component)

    def remove(self, component_class):
        component = self.get(component_class)
        if component is not None:
            component.entity = None
            self.components.remove(component)

    def has(self, component_class):
        for component in self.components:
            if isinstance(component, component_class):
                return True
        return False

    def get(self, component_class):
        for component in self.components:
            if isinstance(component, component_class):
                return component
        return None
