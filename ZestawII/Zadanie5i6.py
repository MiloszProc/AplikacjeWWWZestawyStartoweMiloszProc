class Calculator:
    def add(self, number1, number2):
        return number1 + number2

    def difference(self, number1, number2):
        return number1 - number2

    def multiply(self, number1, number2):
        return number1 * number2

    def divide(self, number1, number2):
        return number1 / number2


class ScienceCalculator(Calculator):
    def power(self, number1, number2):
        return pow(number1, number2)


calculator = ScienceCalculator()
print(calculator.add(10, 15))
print(calculator.difference(8, 6))
print(calculator.difference(4, 6))
print(calculator.multiply(4, 6))
print(calculator.divide(6, 2))
print(calculator.power(3, 3))