#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        isLowercase = ord(letter) >= 97 and ord(letter) <= 122
        print("{}".format(chr(ord(letter) - (32 if isLowercase else 0))), end='')
    print("\n", end="")
