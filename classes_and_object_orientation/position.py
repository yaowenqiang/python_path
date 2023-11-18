from icecream import ic
class Position:
    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= +90):
            raise ValueError(f'latitude {latitude} out of range')
        if not (-180 <= latitude <= +180):
            raise ValueError(f'longitude {longitude} out of range')

        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude_hemisphere(self):
        return 'W' if self.latitude >=0 else 'S'

    @property
    def longitude_hemisphere(self):
        return 'E' if self.longitude >=0 else 'W'

    def __repr__(self):
        #return f'{self.__class__.__name__}(latitude={self.latitude}, longitude={self.longitude})'
        return f'{typename(self)}(latitude={self.latitude}, longitude={self.longitude})'

    def __str__(self):
        return format(self)
        return (
            f"{abs(self.latitude)}* {self.latitude_hemisphere}, "
            f"{abs(self.longitude)}* {self.longitude_hemisphere}"
        )

    def __format__(self, format_spec):
        #return 'FORMATTED POSITION'
        component_format_spec= '.2f'
        prefix, dot, suffix = format_spec.partition('.')
        if dot:
            num_decimal_places = int(suffix)
            component_format_spec = f'.{num_decimal_places}f'
        latitude = format(abs(self.latitude), component_format_spec)
        longitude = format(abs(self.longitude), component_format_spec)
        return (
            f"{latitude}* {self.latitude_hemisphere}, "
            f"{longitude}* {self.longitude_hemisphere}"
        )


class EarthPosition(Position):
    pass

class MarsPosition(Position):
    pass

def typename(obj):
    return type(obj).__name__


if __name__ == '__main__':
    position = Position(90, 90)
    ic(position)
    ic(repr(position))
    ic(str(position))
    ic(format(position))
    ic(format(position, '.3'))
    ic(format(position, '.0'))
    ic(f"{position})")
    ic(f"{position!r})")
    ic(f"{position!s})")
    ic(f"{position=})")
    earth_position = EarthPosition(90, 90)
    ic(earth_position)
    marth_position = MarsPosition(50, 50)
    ic(marth_position)

    q = 7.74091e-5
    ic(format(q, 'f'))
    ic(format(q, '.7f'))
    ic(format(q, '+.7f'))
    ic(format(q, '>+20.11f'))
    ic(f'{q}')
    ic(f'{q:.6f}')
    ic(f'{q:.2e}')


