#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
last_string = ''
if last_digit > 5:
    last_string = "and is greater than 5"
elif last_digit < 6 and last_digit != 0:
    last_string = "and is less than 6 and not 0"
else:
    last_string = "and is 0"
print(f"Last digit of {number} is {last_digit} {last_string}")
