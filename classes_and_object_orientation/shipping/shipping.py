class ShppingContainer:
    next_serial = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShppingContainer.next_serial
        ShppingContainer.next_serial += 1

class MyClass:
    b = 'on class'
    def __init__(self):
        self.a = 'on instance'
        print(self.a)
        print(MyClass.b)
        print(self.b)
        self.a = 're-bound'
        self.b = 'new on instance'
        print(self.b)
        print(MyClass.a)

