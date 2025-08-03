active_objs = []

class Entity:
    def __init__(self, *components, x=0, y=0):
        self.components = []
        for component in components:
            self.add(component)
        self.x = x
        self.y = y

    def add(self, component):
        self.components.append(component)
        component.entity = self

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