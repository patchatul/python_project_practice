import unittest
import math
def get_sqrt(n):
    return math.sqrt(n)

class TestUnexpected(unittest.TestCase):
    def test_get_sqrt(self):
        self.assertEqual(get_sqrt(144),12)
            
    def test_get_sqrt_negative(self):
        with self.assertRaises(ValueError):
            get_sqrt(-1)# taking the square root of a negative number raises a ValueErro

if __name__ =='__main__':
    unittest.main()   