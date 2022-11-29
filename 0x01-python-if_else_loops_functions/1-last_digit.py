#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"{number}")
if number < 0:
    last_digit = -number % 10
else:
    last_digit = number % 10

if last_digit > 5:
    print(f"The last digit of {number} is {last_digit} and is greater than 5")
elif:
    print(f"{number % 10}")
