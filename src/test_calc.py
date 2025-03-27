import unittest

from calc import sum


class TestCalc(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(0,0),0)
        self.assertEqual(sum(10,5),15)
        self.assertEqual(sum(-1,2),1)
        self.assertEqual(sum(-1,-1),2)
        

if __name__ == '__main__':
    unittest.main()