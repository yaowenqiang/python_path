from icecream import ic
class A:
    def func(self):
        return 'A.func'

class B(A):
    def func(self):
        return 'B.func'

class C(A):
    def func(self):
        return 'C.func'

class D(B,C):
    pass

class E(C,B):
    pass

if __name__ == '__main__':
    ic(D.__mro__)
    d = D()
    ic(d.func())
    e = E()
    ic(e.func())
