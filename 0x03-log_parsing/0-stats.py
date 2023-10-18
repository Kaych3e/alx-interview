#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""

import sys

"""initialise variables"""
statc = [200, 301, 400, 401, 403, 404, 405, 500]
count = 0
stat_code_map = {}
total_size = 0


def print_stats():
    """prints statistics"""
    print("File size: {}".format(total_size))
    for status, number in sorted(stat_code_map.items()):
        print("{}: {}".format(status, number))


try:
    for line in sys.stdin:
        stat_list = line.split()
        try:
            file_size = int(stat_list[-1])
            total_size += file_size
            stat_code = int(stat_list[-2])
            if stat_code in statc:
                if stat_code in stat_code_map:
                    stat_code_map[stat_code] += 1
                else:
                    stat_code_map[stat_code] = 1
        except ValueError:
            pass
        count += 1
        if count % 10 == 0:
            print_stats()

    if (count == 0) or (count % 10 != 0):
        print_stats()

except KeyboardInterrupt:
    print_stats()
