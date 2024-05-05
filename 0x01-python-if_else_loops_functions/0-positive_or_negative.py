#!/usr/bin/python3
import random

# Assign a random signed number to the variable 'number'
number = random.randint(-10, 10)  # This will assign a number between -10 and 10

# Check if the number is positive or negative and print the result
if number > 0:
    print("The number", number, "is positive.")
elif number < 0:
    print("The number", number, "is negative.")
else:
    print("The number is zero.")
