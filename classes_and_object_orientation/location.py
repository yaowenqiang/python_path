#from utility import typename
from icecream import ic
import inspect

def auto_repr(cls):
    ic(f'Decorating {cls.__name__} with auto_repr')
    members = vars(cls)
    for name, member in members.items():
        ic(name, member)

    if '__repr__' in members:
        raise TypeError(f'{cls.__name__} already defines __repr__')

    if '__init__' not in members:
        raise TypeError(f'{cls.__name__} does not override __init__')

    sig = inspect.signature(cls.__init__)
    parameter_names = list(sig.parameters)[1:]

    if not all(
        isinstance(members.get(name, None), property)
        for name in parameter_names
    ):
        raise TypeError(
            f'Cannot apply auto_repr to {cls.__name__} because not all '
            '__init__ parameters have matching property '
        )

    def synthesized_repr(self):
        return '{typename}({args})'.format(
            typename=type(self), 
            args=', '.join(
                '{name}={value!r}'.format(
                    name=name,
                    value=getattr(self,name)
                ) for name in parameter_names
            )
        )

    setattr(cls, '__repr__', synthesized_repr)

    return cls

@auto_repr
class Location:
    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name


    @property
    def position(self):
        return self._position

    #def __repr__(self):
    #    return f'{type(self)}(name={self._name}, position={self.position})'

    #def __str__(self):
    #    return self.name


class EarthPosition():
    def __init__(self, latitude, longitude):
        self._latitude = latitude
        self._longitude = longitude

    def __repr__(self):
        return f'{type(self)}(latitude={self._latitude}, longitude={self._longitude})'


if __name__ == '__main__':
    hong_kong = Location('Hong Kong', EarthPosition(22.29, 114.16))
    stockholm = Location('Stockholm', EarthPosition(59.33, 18.06))
    cap_town = Location('Cap Town', EarthPosition(-33.93, 18.42))
    rotterdam = Location('Rotterdam', EarthPosition(51.96, 4.47))
    maracaibo = Location('Maracaibo', EarthPosition(10.65, -71.65))
    ic(repr(hong_kong))
