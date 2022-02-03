import math
import sys


class Calculator:

    def __init__(self):

        self.selected_operator = ""

        # Operators as variables

        self.add = self.addition
        self.sub = self.subtraction
        self.mul = self.multiplication
        self.div = self.division
        self.exp = self.exponent
        self.flo = self.floor_division

        self.operators = {
            "+": self.add,
            "-": self.sub,
            "*": self.mul,
            "/": self.div,
            "**": self.exp,
            "//": self.flo,
        }

        operators_display_list = []
        for operator in self.operators:
            operators_display_list.append(operator)
        self.operators_display = " ".join(operators_display_list,)
        operators_display_list = []

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

    def exponent(self, a, b):
        return a ** b

    def floor_division(self, a, b):
        return a // b

    def prompt_user_for_a_number(self, which_operand):
        return float(input(f"Enter your {which_operand} number: "))

    def prompt_user_for_operand(self):
        return self.operators[input(f"Which operation to perform: {self.operators_display} ? ")]

    def continue_this_calculation(self):
        cont = input("\nDo you want to continue (Y / N / EXIT)?").lower()
        if cont == "y" or cont == "yes":
            print("\n")
            return True
        elif cont == "e" or cont == "exit":
            sys.exit()
        else:
            return False
