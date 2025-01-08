class Meta(type):
    def __init__(cls, name, bases, dct):
        cls.attr = 100
    
class Foo(metaclass=Meta):
    pass

class Bar(metaclass=Meta):
    pass

class Qux(metaclass=Meta):
    pass

print(Foo.attr, Bar.attr, Qux.attr)