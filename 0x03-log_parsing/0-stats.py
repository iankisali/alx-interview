#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys

status = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}
sizes = [0]


def print_status():
    """Print the print_status"""
    print('File size: {}'.format(sum(sizes)))
    for codes, count in sorted(status.items()):
        if count:
            print('{}: {}'.format(codes, count))


try:
    for i, line in enumerate(sys.stdin, start=1):
        match = line.rstrip().split()
        try:
            code_status = match[-2]
            file_size = match[-1]
            if code_status in status.keys():
                status[code_status] += 1
            sizes.append(int(file_size))
        except Exception:
            pass
        if i % 10 == 0:
            print_status()
    print_status()
except KeyboardInterrupt:
    print_status()
    raise
