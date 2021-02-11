import unittest
from main import is_odd

class TestIsOdd(unittest.TestCase):
    def test_odd_num(self):
        self.assertTrue(is_odd(3))
    
    def test_is_even(self):
      self.assertFalse(is_odd(0))

if __name__ == '__main__':
    unittest.main()
