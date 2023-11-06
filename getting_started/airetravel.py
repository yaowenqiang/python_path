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


    def _parse_seat(self, seat):
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


        return row, letter


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

        row, letter = self._parse_seat(seat)
        if self._seating[row][letter] is not None:
            raise ValueError(f'Seat {seat} already accupied')
        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        """Reallocate a  passenger to a different seat

        Args:
            from_seat: The existing seat designator for the passenger to be moved
            to_seat: The new seat designator

        """
        from_row, from_letter = self._parse_seat(from_seat)

        if self._seating[from_row][from_letter] is None:
            raise ValueError(f'No passenger is relocated in seat {from_seat}')

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f'Seat {to_seat} already accupies!')
        self._seating[to_row][to_letter]  = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] =  None

    def num_oavailable_seats(self):
        return sum(sum(1 for s in row.values() if s is None) for row in self._seating if row is not None)



    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())


    def _passenger_seats(self):
        """An iterable series of passenger seating locations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f'{row}{letter}')


class AirebusA319:
    def _-init__(self, registration):
        self._registration = registration


    def registration(self):
        return self._registration


    def model(self):
        return 'Airebus A319'

    
    def seating_plan(self):
        return range(1,23), 'ABCDEF'

class Boeing777:
    def _-init__(self, registration):
        self._registration = registration


    def registration(self):
        return self._registration


    def model(self):
        return 'boeing 777'

    
    def seating_plan(self):
        return range(1,56), 'ABCDEFGHJK'



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


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f'| Name: {passenger}' \
            f'   Flight: {flight_number}' \
            f'   Seat: {seat}' \
            f'   Aircraft: {aircraft}' \
            ' |'
    banner = '+' + '-' * (len(output) -2) + '+'
    border = '|' + ' ' * (len(output) -2) + '|'

    lines = [banner, border, output,border, banner ]
    card = '\n'.join(lines)
    print(card)
    print()

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
    f.allocate_seat('11F', 'Yukihiro Matsumoto')
    f.allocate_seat('13F', 'John McCarthy')
    f.allocate_seat('14F', 'Richard Hickey')
    f.allocate_seat('15F', 'Larry Wall')
    ic(f._seating)
    f.relocate_passenger('12A', '18A')
    ic(f._seating)
    ic(f.num_oavailable_seats())
    f.make_boarding_cards(console_card_printer)



