class NamespaceManager:
    def __init__(self):
        self.namespace = {}

    def set_variable(self, name, value):
        self.namespace[name] = value

    def get_variable(self, name):
        if name in self.namespace:
            return self.namespace[name]
        else:
            raise KeyError(f"Variable '{name}' not found")

    def delete_variable(self, name):
        if name in self.namespace:
            del self.namespace[name]
        else:
            raise KeyError(f"Variable '{name}' not found")

    def list_variables(self):
        return list(self.namespace.keys())

    def execute_function(self, code):
        exec(code, {}, self.namespace)
