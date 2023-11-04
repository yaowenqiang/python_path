"""
Model for aircraft flights.
"""
from icecream import ic
class Flight:
    """A flight with a particular passenger aircraft."""
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")
        if not number[:2].isupper():
            raise ValueError(f"No airline code '{number}'")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route  code number '{number}'")

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]


    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    def aireline(self):
        return self._number[2:]

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger

        Args:
            seat: A seat designator such '12C' or '13F',
            passenger: the passenger name.

        Raises:
            ValueError: if the seat is unavailable
        """

        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]

        if letter not in seat_letters:
            raise ValueError(f'Invalid seat letter {letter}')

        row_text  = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid seat row{row_text}')

        if row not in rows:
            raise ValueError(f'Invalid row number {row}')

        if self._seating[row][letter] is not None:
            raise ValueError(f'Seat {seat} already accupied')

        self._seating[row][letter] = passenger



class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row


    def registration(self):
        return self._registration

    def model(self):
        return self._model
    def num_rows(self):
        return self._num_rows
    def num_seats_per_row(self):
        return self._num_seats_per_row


    def seating_plan(self):
        return (range(1, self._num_rows + 1), 'ABCDEFGHJK'[:self._num_seats_per_row])

if __name__  == '__main__':
    a = Aircraft('G-EUPT', 'Airbus A319',num_rows=22, num_seats_per_row=6)
    ic(a)
    ic(a.model())
    ic(a.seating_plan())
    f = Flight('BA758', Aircraft('G-EUPT', 'Airbus A219',num_rows=22, num_seats_per_row=6))
    ic(f.aircraft_model())
    ic(f._seating)
    f.allocate_seat('12B', 'jacky')
    f.allocate_seat('12A', 'Guidu van Rossum')
    f.allocate_seat('12C', 'Rasmus Lerdorf')
    f.allocate_seat('11C', 'Bjarne Stroustrup')
    f.allocate_seat('11D', 'Anders Hejlsberg')
    f.allocate_seat('11f', 'Yukihiro Matsumoto')
    f.allocate_seat('13f', 'John McCarthy')
    f.allocate_seat('14f', 'Richard Hickey')
    f.allocate_seat('15f', 'Larry Wall')
    ic(f._seating)



