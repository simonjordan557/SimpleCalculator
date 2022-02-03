# Simple Calculator

from calculator import Calculator
import os

calc = Calculator()
is_on = True
continue_calculation = True

while is_on:
    os.system("cls")
    print("Welcome To Simple Calculator!\n")
    continue_calculation = True
    x = calc.prompt_user_for_a_number("first")
    while continue_calculation:
        o = calc.prompt_user_for_operand()
        y = calc.prompt_user_for_a_number("second")
        answer = o(x, y)
        print(f"\nThe answer is: {answer}")
        continue_calculation = calc.continue_this_calculation()
        if continue_calculation:
            x = answer
        else:
            break


