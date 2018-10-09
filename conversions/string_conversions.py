from .utils import str_to_int


def _to_string(value, prefix, encoding):
    result = []
    if not prefix:
        if value.startswith('0x'):
            value = value.replace('0x', '')
            prefix = '0x'
        elif value.startswith('0b'):
            value = value.replace('0b', '')
            prefix = '0b'
        elif value.startswith('0o'):
            value = value.replace('0o', '')
            prefix = '0o'
    try:
        for i in range(0, len(value), 2):
            result.append(chr(str_to_int(prefix + value[i:i + 2])))
        return ''.join(result)
    except ValueError:
        value = value.encode("raw_unicode_escape").decode(encoding)
        return value


def get_string(value, prefix='', encoding='utf-8'):
    if isinstance(value, int):
        return chr(value)
    elif isinstance(value, str):
        return _to_string(value, prefix, encoding)
    elif isinstance(value, bytes):
        value = value.decode(encoding)
        return _to_string(value, prefix, encoding)
