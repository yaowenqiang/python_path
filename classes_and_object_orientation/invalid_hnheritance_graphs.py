class A:
    pass
class B(A):
    pass
class C(A):
    pass

class D(B, A, C):
    pass

