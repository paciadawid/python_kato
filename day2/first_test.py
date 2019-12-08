import unittest
from hamcrest import *

class FirstTests(unittest.TestCase):

    def test_1(self):
        assert_that(1+1, equal_to(2))

    def test_2(self):
        assert_that(1+2, equal_to(4))

if __name__ == "__main__":
    unittest.main()
