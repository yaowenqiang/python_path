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


if __name__ == '__main__':
    unittest.main()

    for i,j in enumerate(range(2**4, 2**5)):
        print(f'{i:2} {i:05b}       {j:2} {j:05b}')