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

    def __repr__(self):
        #return f'{self.__class__.__name__}(latitude={self.latitude}, longitude={self.longitude})'
        return f'{typename(self)}(latitude={self.latitude}, longitude={self.longitude})'


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
    earth_position = EarthPosition(90, 90)
    ic(earth_position)
    marth_position = MarsPosition(50, 50)
    ic(marth_position)

