# Test the functions in the a4.py file
import unittest
from a4 import Utils

class TestA4(unittest.TestCase):
        
        def test_reversed(self):

            # Test with int
            self.assertEqual(Utils.reversed(123), 321)
            self.assertEqual(Utils.reversed(-123), -321)
            self.assertEqual(Utils.reversed(120), 21)

            # Test with float
            self.assertRaises(TypeError, Utils.reversed, 1.0)

            # Test with string
            self.assertRaises(TypeError, Utils.reversed, "1")

        def test_formatter(self):

            # Test with int
            self.assertEqual(Utils.formatter(10), ('0b1010', '0o12'))
            self.assertEqual(Utils.formatter(-10), ('-0b1010', '-0o12'))
            self.assertEqual(Utils.formatter(123), ('0b1111011', '0o173'))

            # Test with float
            self.assertRaises(TypeError, Utils.formatter, 1.0)

            # Test with string
            self.assertRaises(TypeError, Utils.formatter, "1")

if __name__ == "__main__":
    unittest.main()