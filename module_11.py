
def introspection_info(obj):
    obj_type = type(obj).__name__

    obj_dir = dir(obj)

    methods = [item for item in obj_dir if callable(getattr(obj, item)) and not item.startswith('__')]
    attributes = [item for item in obj_dir if not callable(getattr(obj, item)) and not item.startswith('__')]

    obj_module = getattr(obj, '__module__', 'built-in')

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }

    return info

class Example:
    def __init__(self, value):
        self.value = value

    def example_method(self):
        return self.value

example_obj = Example(42)

introspection_result = introspection_info(example_obj)
print(introspection_result)
