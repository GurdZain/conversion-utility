from conversions.utils import str_to_int, string_to_ascii


def _guess_type(value, prefix, encoding, func=None):
    if isinstance(value, int):
        return func(value) if func else value
    elif isinstance(value, str):
        value = prefix + value if prefix else value
        return func(str_to_int(value)) if func else str_to_int(value)
    elif isinstance(value, bytes):
        value = value.decode(encoding)
        value = string_to_ascii(value)
        return func(str_to_int(value)) if func else str_to_int(value)


def to_int(value, prefix='', encoding='utf-8'):
    return _guess_type(value, prefix, encoding)


def to_binary(value, prefix='', encoding='utf-8'):
    return _guess_type(value, prefix, encoding, bin)


def to_octal(value, prefix='', encoding='utf-8'):
    return _guess_type(value, prefix, encoding, oct)


def to_decimal(value, prefix='', encoding='utf-8'):
    return _guess_type(value, prefix, encoding, str)


def to_hexadecimal(value, prefix='', encoding='utf-8'):
    return _guess_type(value, prefix, encoding, hex)
