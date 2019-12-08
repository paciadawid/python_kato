class BasicCalculator:

    def add(self, a, b):
        result = a + b
        return result
    def odejmowanie(self, a, b):
        result = a - b
        return result
    def mnozenie(self, a, b):
        result = a * b
        return result
    def dzielenie(self, a, b):
        if b == 0:
            return False
        else:
            result = a / b
            return result
    def zero_error(self):
        a = 1/0

#if __name__ == "__main__":
#    calculator = BasicCalculator()
#    sum = calculator.add(1, 2)
#    print("wynik sumowania wynosi", sum)

#odej= calculator.odejmowanie(1, 2)
#print("wynik odejmowaniawynosi", odej)


#mno = calculator.mnozenie(1, 2)
#print("wynik mnozenia wynosi", mno)


#dziel = calculator.dzielenie(1, 0)
#print("wynik dzielenia wynosi", dziel)

