from day1.methods_and_classes.src.calculator import BasicCalculator
from hamcrest import *

calculator = BasicCalculator()

assert calculator.add(1, 2) == 3, "wrong value"

assert_that(calculator.add(1, 2), equal_to(3))
assert_that(calculator.odejmowanie(2, 1), equal_to(1))
assert_that(calculator.mnozenie(2, "a"), equal_to(4))
assert_that(calculator.dzielenie(2, 2), equal_to(1))


