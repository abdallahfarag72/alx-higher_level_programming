#!/usr/bin/python3

"""
Defines a script that reads stdin
line by line and computes metrics
"""


import sys

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_count = {code: 0 for code in status_codes}
file_size = 0
line_count = 0

try:
    for i, line in enumerate(sys.stdin, 1):
        data = line.split()
        if len(data) >= 2:
            file_size += int(data[-1])
            status = data[-2]
            if status in status_count:
                status_count[status] += 1

        if i % 10 == 0:
            print("File size: {:d}".format(file_size))
            for code, count in sorted(status_count.items()):
                if count > 0:
                    print("{:s}: {:d}".format(code, count))

except KeyboardInterrupt:
    pass

finally:
    print("File size: {:d}".format(file_size))
    for code, count in sorted(status_count.items()):
        if count > 0:
            print("{:s}: {:d}".format(code, count))
