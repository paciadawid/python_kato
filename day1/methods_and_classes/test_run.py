from day1.methods_and_classes.src.factorial import factorial

print(factorial("o"))

try:
    factorial()
except BaseException as err:
    print(err)

#calculator = BasicCalculator()
#print(calculator.add(1, 2))


