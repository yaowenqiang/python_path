class A:
    def func(self):
        print('A')
class B:
    def func(self):
        print('B')

a = A()
a.func()
a.__class__ = B
a.func()
# B
