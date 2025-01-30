# A custom metaclass example
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['meta_info'] = 'This is a custom metaclass'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

# Accessing the added attribute from metaclass
print(MyClass.meta_info)
