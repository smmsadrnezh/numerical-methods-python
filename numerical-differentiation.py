"""numerical_differentiation.py:  Calculate second numerical differentiation of a function using numerical methods."""
from math import sqrt

__author__ = "Masoud Sadrnezhaad"

# Read the input

x = float(input("Point: "))
function = input("Enter the function: ")
error = float(input("Error: "))

func_x = eval(function)

# Calculate numerical differentiation
h = sqrt(abs(- (12 * error) / (func_x ** 4)))

x += h
func_xh = eval(function)
x -= 2 * h
func_hx = eval(function)

answer = (func_xh - 2 * func_x + func_hx) / (h ** 2)
print("Answer: " + str(answer))
