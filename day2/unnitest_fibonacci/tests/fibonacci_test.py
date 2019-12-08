from day2.unnitest_fibonacci.src.fibonacci import fibonacci1
import unittest
from hamcrest import *


class FibonacciTest(unittest.TestCase):

    def test_first_element(self):
        assert_that(fibonacci1(1), equal_to(0))

    def test_second_element(self):
        assert_that(fibonacci1(2), equal_to(1))

    def test_negative_value(self):
        assert_that(fibonacci1(-1), equal_to(False))

    def test_letter(self):
        assert_that(fibonacci1("a"), equal_to(False))

    def test_positive_path(self):
        assert_that(fibonacci1(5), 3)

    def test_large_value(self):
        assert_that(fibonacci1(100000000000), equal_to(False))

if __name__ == "__main__":
    unittest.main()

