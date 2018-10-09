def str_to_int(value):
    if value.startswith('0x'):
        value = value.replace('0x', '')
        return int(value, 16)
    elif value.startswith('0b'):
        value = value.replace('0b', '')
        return int(value, 2)
    elif value.startswith('0o'):
        value = value.replace('0o', '')
        return int(value, 8)
    else:
        return int(value, 10)


def string_to_ascii(value):
    result = []
    for s in value:
        result.append(hex(ord(s)))
    return ''.join(result)
