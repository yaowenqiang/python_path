from bitfield import BitFieldMeta
import unittest

class TestBitField(unittest.TestCase):
    """Test BitfieldMeta and the bitfield classes it makes"""

    def test_define_bitfield(self):
        class DateBitField(metaclass=BitFieldMeta):
            day: 5

    def test_instantiate_default_bitfield(self):
        class DateBitField(metaclass=BitFieldMeta):
            day: 5

        _ = DateBitField(day=23)

    def test_bitfield_without_fields_raises_type_error(self):
        with self.assertRaises(TypeError):
            class DateBitField(metaclass=BitFieldMeta):
                pass

    def test_mismatched_constructor_argument_names_raises_type_error(self):
        class DateBitField(metaclass=BitFieldMeta):
            day: 5
            month: 4
            year: 14

        with self.assertRaises(TypeError) as exc_info:
            _ = DateBitField(day=13, mnth=5, yr=1999)

        self.assertEqual(
            str(exc_info.exception),
            "DateBitField.__init__() got unexpected keyword arguments: "
            "'mnth', 'yr'"
        )

    def test_non_integer_annotation_value_types_raises_type_error(self):
        with self.assertRaises(TypeError) as exc_info:
            class DateBitField(metaclass=BitFieldMeta):
                day: 'Wednesday'

        self.assertEqual(
            str(exc_info.exception),
            "DateBitField field day has annotation 'Wednesday' "
            "that is not an integer")

    def test_zero_field_width_raises_type_error(self):
        with self.assertRaises(TypeError) as exc_info:
            class DateBitField(metaclass=BitFieldMeta):
                day: 0

        self.assertEqual(
            str(exc_info.exception),
            "DateBitField field day has non-positive field width 0"
        )
    def test_negative_field_width_raises_type_error(self):
        with self.assertRaises(TypeError) as exc_info:
            class DateBitField(metaclass=BitFieldMeta):
                day: -1

        self.assertEqual(
            str(exc_info.exception),
            "DateBitField field day has non-positive field width -1"
        )

    def test_field_name_with_leading_underscore_raises_type_error(self):
        with self.assertRaises(TypeError) as exc_info:
            class DateBitField(metaclass=BitFieldMeta):
                _day: 5

        self.assertEqual(
            str(exc_info.exception),
            "DateBitField field _day begins with an underscore"
        )

    def test_initialization_out_of_lower_field_range_raises_value_error(self):
        class DateBitField(metaclass=BitFieldMeta):
            day: 5

        with self.assertRaises(ValueError) as exc_info:
            _ = DateBitField(day=-1)

        self.assertEqual(
            str(exc_info.exception),
            "DateBitField field 'day' got value -1 "
            'which is out of range 0-31 for a 5-bit field'
        )

    def test_initialization_out_of_upper_field_range_raises_value_error(self):
        class DateBitField(metaclass=BitFieldMeta):
            day: 5

        with self.assertRaises(ValueError) as exc_info:
            _ = DateBitField(day=32)

        self.assertEqual(
            str(exc_info.exception),
            "DateBitField field 'day' got value 32 "
            'which is out of range 0-31 for a 5-bit field'
        )

    def test_fields_are_default_initialized_to_zero(self):
        class DateBitField(metaclass=BitFieldMeta):
            day: 5

        d = DateBitField()
        self.assertEqual(d.day, 0)

    def test_initialized_field_values_can_be_retrived(self):
        class DateBitField(metaclass=BitFieldMeta):
            day: 5

        d = DateBitField(day=17)
        self.assertEqual(d.day, 17)

    def test_conversion_to_integers(self):
        class DateBitField(metaclass=BitFieldMeta):
            day: 5

        d = DateBitField(day=17)
        self.assertEqual(d.to_int(), 17)

    def test_conversion_to_integers(self):
        class DateBitField(metaclass=BitFieldMeta):
            day: 5
            month: 4
            year: 24

        d = DateBitField(day=25, month=3, year=2010)
        i = int(d)
        self.assertEqual(i, 0b111111000100_100_11001)



    def test_conversion_to_bytes(self):
        class DateBitField(metaclass=BitFieldMeta):
            day: 5
            month: 4
            year: 24

        d = DateBitField(day=25, month=3, year=2010)
        b = d.to_bytes()
        self.assertEqual(
            b,
            (0b111111000100_100_11001).to_bytes(3, 'little', signed=False)
        )


    def test_assigning_to_field_sets_value(self):
        class DateBitField(metaclass=BitFieldMeta):
            day: 5

        d = DateBitField(day=25)
        d.day = 26
        self.assertEqual(
            d.day,
            26
        )

    def test_assigning_out_of_lower_range_value_to_field_raises_value_error(self):
        class DateBitField(metaclass=BitFieldMeta):
            day: 5

        d = DateBitField(day=25)
        with self.assertRaises(ValueError) as exc_info:
            d.day = -1

        self.assertEqual(
            str(exc_info.exception),
            "DateBitField field 'day' got value -1 which is out of range 0-31 for a 5-bit field"
        )

    def test_assigning_out_of_upper_range_value_to_field_raises_value_error(self):
        class DateBitField(metaclass=BitFieldMeta):
            day: 5

        d = DateBitField(day=25)
        with self.assertRaises(ValueError) as exc_info:
            d.day = 32

        self.assertEqual(
            str(exc_info.exception),
            "DateBitField field 'day' got value 32 which is out of range 0-31 for a 5-bit field"
        )

if __name__ == '__main__':
    unittest.main()

    for i,j in enumerate(range(2**4, 2**5)):
        print(f'{i:2} {i:05b}       {j:2} {j:05b}')