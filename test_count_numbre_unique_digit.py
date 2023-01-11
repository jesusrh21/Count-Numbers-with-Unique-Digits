import unittest
from count_numbre_unique_digit import Solution as cnud

class test_Solution(unittest.TestCase):
    def test_countNumbersWithUniqueDigits(self):
        self.assertEqual(cnud.countNumbersWithUniqueDigits(self,n=2),91)
        self.assertEqual(cnud.countNumbersWithUniqueDigits(self,n=0),1)
        self.assertEqual(cnud.countNumbersWithUniqueDigits(self,n=3),739)

if __name__ == '__main__()':
    unittest.main()