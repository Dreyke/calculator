__author__ = 'Dreyke Boone'

# calculator class with basic math functions
class Calculator:

    def __init__(self):
        self._answer = 0.0

    @property
    def answer(self):
        return self._answer

    def addition(self, a, b):
        self._answer = a + b
        return self.answer

    def subtraction(self, a, b):
        self._answer = a - b
        return self.answer

    def multiplication(self, a, b):
        self._answer = a * b
        return self.answer

    def division(self, a, b):
        self._answer = a * 1.0 / b
        return self.answer

# main method to accept user input
def main():

    calculator = Calculator()
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter a second number: "))

    selection = input("Do you want to add, subtract, multiply, or divide these numbers?\n"
                          "1. Add\n"
                          "2. Subtract\n"
                          "3. Multiply\n"
                          "4. Divide\n")

    # loop to determine which math function to call
    if selection == '1':
        print("Answer:", calculator.addition(number_1, number_2))
    elif selection == '2':
        print("Answer:", calculator.subtraction(number_1, number_2))
    elif selection == '3':
        print("Answer:", calculator.multiplication(number_1, number_2))
    elif selection == '4':
        print("Answer:", calculator.division(number_1, number_2))
    else:
        print("Please select a valid option.")

main()