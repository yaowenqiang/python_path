class MetaA(type):
    pass


class MetaB(type):
    pass
class MetaC(MetaA, MetaB):
    pass

class A(metaclass=MetaA):
    def __init__(self):
        print('init from a')
    pass

class B(metaclass=MetaB):
    def __init__(self):
        print('init from B')
    pass

# class C(A,B):
class C(A, B, metaclass=MetaC):

    def __init__(self):
        super().__init__()
        print('init from C')
    pass

class D(A):
    pass


