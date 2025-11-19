def add(number1, number2):
    return number1 + number2

def multiply(number1, number2):
    return number1 * number2

class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def subtract(self):
        return self.number1 - self.number2