#!/usr/bin/python3
"""
Script reads log lines from stdin, computes metrics, and prints statistics
based on the specified log format.
"""

import sys
from collections import defaultdict


def parse_line(line):
    """
    Parse the given log line.

    Args:
    line (str): Log line to be parsed.

    Returns:
    tuple: A tuple containing the status code and file size if the line matches
    the expected format, otherwise (None, None).
    """
    parts = line.split()
    if len(parts) >= 9:
        status_code = parts[-2]
        try:
            status_code = int(status_code)
            if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
                file_size = int(parts[-1])
                return status_code, file_size
        except ValueError:
            pass
    return None, None


def print_statistics(total_size, status_counts):
    """
    Print the aggregated statistics.

    Args:
    total_size (int): Total accumulated file size.
    status_counts (dict): Dictionary containing counts of status codes.
    """
    print(f'Total file size: {total_size}')
    for code in sorted(status_counts.keys()):
        print(f'{code}: {status_counts[code]}')


def main():
    """
    Main function to process log lines from stdin and print statistics.
    """
    lines_processed = 0
    total_size = 0
    status_counts = defaultdict(int)

    try:
        for line in sys.stdin:
            line = line.strip()
            status_code, file_size = parse_line(line)
            if status_code is not None and file_size is not None:
                lines_processed += 1
                total_size += file_size
                status_counts[status_code] += 1

                if lines_processed % 10 == 0:
                    print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        sys.exit(0)


if __name__ == "__main__":
    main()
