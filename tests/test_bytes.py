import unittest
import conversions


class TestStr(unittest.TestCase):
    def test_int(self):
        result = conversions.get_bytes(0x41)
        self.assertEqual(result, b'A')

    def test_hex(self):
        result = conversions.get_bytes('0x414141')
        self.assertEqual(result, b'AAA')

    def test_decimal(self):
        result = conversions.get_bytes('656565')
        self.assertEqual(result, b'AAA')

    def test_str(self):
        result = conversions.get_bytes('\x41\x41\x41')
        self.assertEqual(result, b'AAA')

    def test_bytes(self):
        result = conversions.get_bytes(b'\x41\x41\x41')
        self.assertEqual(result, b'AAA')

    def test_bytes_str(self):
        result = conversions.get_bytes(b'414141', prefix='0x')
        self.assertEqual(result, b'AAA')

    def test_encode(self):
        result = conversions.get_bytes('filename=\xd3\xf1\xc1\xfa', encoding='gbk')
        self.assertEqual(result, b'filename=\xd3\xf1\xc1\xfa')

    def test_unicode(self):
        result = conversions.get_bytes('filename=\xd3\xf1\xc1\xfa', encoding='gbk')
        self.assertEqual(result, b'filename=\xd3\xf1\xc1\xfa')
