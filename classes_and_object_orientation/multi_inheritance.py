class Base1():
    def __init__(self):
        print('Base1.__init__')

class Base2():
    def __init__(self):
        print('Base2.__init__')

class Sub(Base1, Base2):
    pass



if __name__ == '__main__':
    s = Sub()


