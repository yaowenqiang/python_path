#from utility import typename
from icecream import ic
import inspect
import functools

def postcondition(predicate):
    def function_decorator(f):
        @functools.wraps(f)
        def wrapper(self, *args, **kwargs):
            result = f(self, *args, **kwargs)
            if not predicate(self):
                raise RuntimeError(
                    f'Post-condition {predicate.__name__} not '
                    f'maintained for {self!r}'
                )
            return result
        return wrapper
    return function_decorator

def no_duplicates(itinerary):
    already_seen = set()
    for location in itinerary._locations:
        if location in already_seen:
            return False
        already_seen.add(location)
    return True

def invariant(predicate):
    function_decorator = postcondition(predicate)

    def class_decorator(cls):
        members = list(vars(cls).items())

        for name, member in members:
            if inspect.isfunction(member):
                decorated_member = function_decorator(member)
                setattr(cls, name, decorated_member)
        return cls

    return class_decorator

def at_least_two_locations(itinerary):
    return len(itinerary._locations) >= 2


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

@auto_repr
@invariant(no_duplicates)
@invariant(at_least_two_locations)
class Iteinerary:
    @classmethod
    def from_locations(cls, *locations):
        return cls(locations)

    #@postcondition(at_least_two_locations)
    def __init__(self, locations):
        self._locations = list(locations)

    def __str__(self):
        return '\n'.join(location.name for location in self._locations)

    @property
    def locations(self):
        return tuple(self._locations)

    @property
    def origin(self):
        return self._locations[0]

    @property
    def destination(self):
        return self._locations[-1]

    #@postcondition(at_least_two_locations)
    def add(self, location):
        self._locations.append(location)

    #@postcondition(at_least_two_locations)
    def remove(self, name):
        removal_indexes = [
            index for index, location in enumerate(self._locations)
            if location.name == name
        ]
        for index in reversed(removal_indexes):
            del self._locations[index]

    #@postcondition(at_least_two_locations)
    def truncate_at(self, name):
        stop = None
        for index, location in enumerate(self._locations):
            if location.name == name:
                stop = index + 1
                self._locations = self._locations[:stop]

if __name__ == '__main__':
    hong_kong = Location('Hong Kong', EarthPosition(22.29, 114.16))
    stockholm = Location('Stockholm', EarthPosition(59.33, 18.06))
    cap_town = Location('Cap Town', EarthPosition(-33.93, 18.42))
    rotterdam = Location('Rotterdam', EarthPosition(51.96, 4.47))
    maracaibo = Location('Maracaibo', EarthPosition(10.65, -71.65))
    ic(repr(hong_kong))

    trip = Iteinerary.from_locations(maracaibo, rotterdam, stockholm)
    ic(trip)
    ic(str(trip))
    ic(trip.locations)
    ic(trip.origin)
    ic(trip.destination)
    trip.add(hong_kong)
    ic(str(trip))
    trip.remove('Stockholm')
    ic(str(trip))
    trip.truncate_at('Rotterdam')
    ic(str(trip))

    #trip2 = Iteinerary.from_locations(maracaibo)
    trip2 = Iteinerary.from_locations(maracaibo,stockholm)
    #trip2.add(stockholm)
