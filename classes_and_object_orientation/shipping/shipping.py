# ISO6346 BIC Code Category identifier(Bureau International des Container)
import iso6346
from icecream import ic
class ShppingContainer:
    next_serial = 1337

    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    def __init__(self, owner_code, length_ft, contents, **kwargs):
        self.owner_code = owner_code
        self.length_ft = length_ft
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
    def create_empty(cls, owner_code, length_ft,  **kwargs):
        return cls(owner_code,length_ft, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), **kwargs)

    @property
    def volume_ft3(self):
        return ShppingContainer.HEIGHT_FT * ShppingContainer.WIDTH_FT * self.length_ft


class RefrigerateShippingContainer(ShppingContainer):

    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    def __init__(self, owner_code, length_ft, contents, *, celsius, **kwargs):
        super().__init__(owner_code, length_ft, contents, **kwargs)
        #if celsius > RefrigerateShippingContainer.MAX_CELSIUS:
        #    raise ValueError('Temperature too hot!')
        self.celsius = celsius


    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > RefrigerateShippingContainer.MAX_CELSIUS:
            raise ValueError('Temperature too hot!')
        self._celsius = value

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @property
    def fahrenheit(self):
        return RefrigerateShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigerateShippingContainer._f_to_c(value)

    def get_celsius(self):
        return self._celsius

    def set_celsius(self, value):
        if value > RefrigerateShippingContainer.MAX_CELSIUS:
            raise ValueError('Temperature too hot!')
        self._celsius = value


    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R'
        )

    @property
    def volume_ft3(self):
        return (
            #self.length_ft
            #* ShppingContainer.HEIGHT_FT
            #* ShppingContainer.WIDTH_FT
            super().volume_ft3
            - RefrigerateShippingContainer.FRIDGE_VOLUME_FT3
        )

class HeatedRefrigeratedShippingcontainer(RefrigerateShippingContainer):
    MIN_CELSIUS = -20


    #@celsius.setter
    @RefrigerateShippingContainer.celsius.setter
    def celsius(self, value):
        if not (
            HeatedRefrigeratedShippingcontainer.MIN_CELSIUS 
            <= value
            <= RefrigerateShippingContainer.MAX_CELSIUS
        ):
            raise ValueError('Temperature out of range')

        self._celsius = value

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
    sc1 = ShppingContainer('YML', 20, 1)
    ic(sc1.bic)
    c7 = ShppingContainer.create_empty('YML', 20)
    ic(c7)

    #c8 = ShppingContainer.create_with_items('MAE',{'food','textiles', 'minerals' })
    c8 = ShppingContainer.create_with_items('MAE',20, {'food','纺织品', '矿物' })
    ic(c8.contents)
    ic(c8.volume_ft3)

    r1 = RefrigerateShippingContainer('MAE', 20, ['fish'], celsius=2.0)
    ic(r1.bic)
    ic(r1.celsius)
    r1.celsius = 3.0
    r1._celsius = 5.0
    #r1.celsius = 5.0
    ic(r1.celsius)
    ic(r1.fahrenheit)
    r1.fahrenheit = -10.0
    ic(r1.celsius)
