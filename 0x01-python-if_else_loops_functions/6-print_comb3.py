#!/usr/bin/python3
for i in range(1, 100):
    isNotUnique = False
    for j in range(0, i):
        if (((j // 10 == i % 10) and (i // 10 == j % 10)) or (i % 11 == 0)):
            isNotUnique = True
    if isNotUnique:
        continue
    if i != 89:
        print("{:02d}, ".format(i), end='')
        continue
    print("{:02d}".format(i))
