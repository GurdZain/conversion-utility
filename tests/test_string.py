import unittest
import conversions


class TestStr(unittest.TestCase):
    def test_int(self):
        result = conversions.get_string(0x41)
        self.assertEqual(result, 'A')

    def test_hex(self):
        result = conversions.get_string('0x414141')
        self.assertEqual(result, 'AAA')

    def test_decimal(self):
        result = conversions.get_string('656565')
        self.assertEqual(result, 'AAA')

    def test_str(self):
        result = conversions.get_string('\x41\x41\x41')
        self.assertEqual(result, 'AAA')

    def test_bytes(self):
        result = conversions.get_string(b'\x41\x41\x41')
        self.assertEqual(result, 'AAA')

    def test_bytes_str(self):
        result = conversions.get_string(b'414141', prefix='0x')
        self.assertEqual(result, 'AAA')

    def test_encode(self):
        result = conversions.get_string('filename=\xd3\xf1\xc1\xfa', encoding='gbk')
        self.assertEqual(result, 'filename=玉龙')

    def test_unicode(self):
        result = conversions.get_string('filename=\xd3\xf1\xc1\xfa', encoding='gbk')
        self.assertEqual(result, 'filename=玉龙')
