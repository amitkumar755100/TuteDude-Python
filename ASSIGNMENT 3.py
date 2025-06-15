# Task 1: Calculate Factorial Using a Function 


# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.


n = int(input("Enter a number:"))

def factorial(f):
    if f < 0:
        return "Factorial is not defined for negative"
    elif f < 2:
        return 1
    else:
        return f * factorial(f-1)

result = factorial(n)
print(f"The factorial of {n} is :",result)






# Task 2: Using the Math Module for Calculations
 
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.
#  Expected Output:
#  For example, if the user enters 25, the output should be:


import math

number  = float(input("Enter a number: " ))

square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)

print("Square root:",square_root)
print("Logarithm",natural_log)
print("Sin: ", sine_value)

    