#!/usr/bin/python3

"""
Defines a script that reads stdin
line by line and computes metrics
"""


import sys


def print_stats(total_size, status_codes):
    """Print the computed statistics"""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))


def update_stats(line, total_size, status_codes):
    """Update the statistics based on a line of input"""
    try:
        parts = line.split()
        size = int(parts[-1])
        code = int(parts[-2])
        total_size += size
        if code in status_codes:
            status_codes[code] += 1
        else:
            status_codes[code] = 1
    except (ValueError, IndexError):
        pass
    return total_size, status_codes


def compute_metrics():
    """Compute metrics from input lines"""
    count = 0
    total_size = 0
    status_codes = {}

    try:
        for line in sys.stdin:
            total_size, status_codes = update_stats(
                line, total_size, status_codes)
            count += 1
            if count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


compute_metrics()
