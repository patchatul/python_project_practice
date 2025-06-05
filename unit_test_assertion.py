import unittest

def reverve_string(s):
    return s[::-1]

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverve_string('moji'), 'ijom') #OK
    def test_in_word(self):
        self.assertEqual(len('world'), 5)

if __name__ == '__main__':
    unittest.main()