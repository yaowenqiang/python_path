# ISO6346 BIC Code Category identifier(Bureau International des Container)
import iso6346
from icecream import ic
class ShppingContainer:
    next_serial = 1337

    def __init__(self, owner_code, contents, **kwargs):
        self.owner_code = owner_code
        self.contents = contents
       #self.serial = ShppingContainer._generate_serial()
        #self.bic = ShppingContainer._make_bic_code(
        self.bic = self._make_bic_code(
            owner_code = owner_code,
            serial=ShppingContainer._generate_serial_()
        )


    @staticmethod
    def _generate_serial():
        ic('staticmethod')
        result = ShppingContainer.next_serial
        ShppingContainer.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )

    @classmethod
    def _generate_serial_(cls):
        ic('classmethod')
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code, **kwargs):
        return cls(owner_code,contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, **kwargs):
        return cls(owner_code, contents=list(items), **kwargs)

class RefrigerateShippingContainer(ShppingContainer):

    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, contents, *, celsius, **kwargs):
        super().__init__(owner_code, contents, **kwargs)
        if celsius > RefrigerateShippingContainer.MAX_CELSIUS:
            raise ValueError('Temperature too hot!')
        self.celsius = celsius


    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R'
        )

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



if __name__ == '__main__':
    sc1 = ShppingContainer('YML', 1)
    ic(sc1.bic)
    c7 = ShppingContainer.create_empty('YML')
    ic(c7)

    #c8 = ShppingContainer.create_with_items('MAE',{'food','textiles', 'minerals' })
    c8 = ShppingContainer.create_with_items('MAE',{'food','纺织品', '矿物' })
    ic(c8.contents)

    r1 = RefrigerateShippingContainer('MAE', ['fish'], celsius=2.0)
    ic(r1.bic)
