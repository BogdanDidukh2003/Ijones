import unittest

from main import *


class TestIjones(unittest.TestCase):

    def setUp(self):
        self.input1 = ["aaa", "cab", "def"]
        self.input2 = ["abcdefaghi"]
        self.input3 = ["aaaaaaa", "aaaaaaa", "aaaaaaa", "aaaaaaa", "aaaaaaa", "aaaaaaa"]
        self.output1 = 5
        self.output2 = 2
        self.output3 = 201684

    def test_ijones(self):
        self.assertTrue(start_counting(self.input1), self.output1)
        self.assertTrue(start_counting(self.input2), self.output2)
        self.assertTrue(start_counting(self.input3), self.output3)


if __name__ == "__main__":
    unittest.main()