from icecream import ic

class BitFieldBase:
    def __init__(self, **kwargs):
        self._validate_arg_names(kwargs)
        self._validate_arg_values(kwargs)

    def _validate_arg_names(self, kwargs):
        mismatched_args = set(kwargs).difference(type(self)._field_widths)
        if len(mismatched_args) > 0:
            raise TypeError(
                "{}.__init__() got unexpected keyword argument{}: {}".format(
                    type(self).__name__,
                    "" if len(mismatched_args) == 1 else "s",
                    ", ".join(repr(arg_name) for arg_name in kwargs if arg_name in mismatched_args)
                )
            )

    def _validate_arg_values(self, kwargs):
        for keyword, value in kwargs.items():
            width = type(self)._field_widths[keyword]
            min_value = 0
            max_value = 2 ** width -1
            if not (min_value <= value <= max_value):
                raise ValueError(
                    f'{type(self).__name__} field {keyword!r} '
                    f'got value {value!r} which is out of '
                    f'range {min_value}-{max_value} for a {width}-bit field'
                )
class BitFieldMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        ic(mcs)
        ic(name)
        ic(bases)
        ic(namespace)
        ic(kwargs)
        field_widths = namespace.get('__annotations__', {})
        if len(field_widths) == 0:
            raise TypeError(f'{name} with metaclass{mcs.__name__} has no fields')

        for field_name, width in field_widths.items():
            if field_name.startswith('_'):
                raise TypeError(f'{name} field {field_name} begins with an underscore')
            if not isinstance(width, int):
                raise TypeError(f'{name} field {field_name} has annotation '
                                f"{width!r} that is not an integer"
                                )
        if width < 1:
            raise TypeError(f'{name} field {field_name} has non-positive '
                            f"field width {width}"
                            )


        namespace['_field_widths'] = field_widths
        bases = (BitFieldBase, ) + bases
        return super().__new__(mcs, name, bases, namespace)



