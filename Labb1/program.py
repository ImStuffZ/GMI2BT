from modules import remnant_numbers as rn
from modules import try_input

print("\nThis program will output a list of all numbers between 1 and 1000,\nwhich when devided with both of your inputs will result in an integer.\n")
print("Enter number 1:")
number1 = input()
print("Enter number 2:")
number2 = input()

rn(number1, number2)

print("\nTry to guess which number between 1 and 100 I have chosen.\n")

try_input()
