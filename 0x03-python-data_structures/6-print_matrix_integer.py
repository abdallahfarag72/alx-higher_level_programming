#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            print("{:d}{}".format(num, " " if num != row[-1] else ""), end="")
        print("")
