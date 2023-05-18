#!/usr/bin/python3
def max_integer(my_list=[]):
    maximum = 0
    for num in my_list:
        if num > maximum:
            maximum = num
    return maximum if len(my_list) > 0 else None
