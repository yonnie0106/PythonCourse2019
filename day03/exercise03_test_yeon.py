import unittest
import exercise03_yeon

class MyExTest(unittest.TestCase):

    def test_count_vowels(self):
        self.assertEqual(exercise03_yeon.count_vowels('abcde'), 2)
        with self.assertRaises(TypeError):
            exercise03_yeon.count_vowels(100)

if __name__ == '__main__':
  unittest.main()
