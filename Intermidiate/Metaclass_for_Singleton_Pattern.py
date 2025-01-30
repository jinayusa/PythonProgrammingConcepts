# Metaclass to enforce Singleton Pattern
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# Singleton class using the SingletonMeta metaclass
class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Testing Singleton behavior
obj1 = SingletonClass("First")
obj2 = SingletonClass("Second")

print(obj1.value)  # Output: First
print(obj2.value)  # Output: First (same instance)
