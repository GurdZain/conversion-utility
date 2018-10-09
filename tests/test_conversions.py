import unittest
import conversions


class TestInt(unittest.TestCase):
    def test_int(self):
        result = conversions.to_int(0x414141)
        self.assertEqual(result, 4276545)

    def test_to_binary(self):
        result = conversions.to_binary(0x414141)
        self.assertEqual(result, '0b10000010100000101000001')


class TestStr(unittest.TestCase):
    def test_int(self):
        result = conversions.to_int('0x414141')
        self.assertEqual(result, 4276545)

    def test_to_binary(self):
        result = conversions.to_binary('0x414141')
        self.assertEqual(result, '0b10000010100000101000001')


class TestBytes(unittest.TestCase):
    def test_int(self):
        result = conversions.to_int(b'\x41\x41\x41')
        self.assertEqual(result, 4276545)

    def test_to_binary(self):
        result = conversions.to_binary(b'\x41\x41\x41')
        self.assertEqual(result, '0b10000010100000101000001')
