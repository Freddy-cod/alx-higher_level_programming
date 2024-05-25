#!/usr/bin/python3
import sys
import signal

def print_stats(total_size, status_counts):
    print(f"File size: {total_size}")
    for status in sorted(status_counts):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def signal_handler(sig, frame):
    print_stats(total_size, status_counts)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 6:
            try:
                size = int(parts[-1])
                status = int(parts[-2])
                total_size += size
                if status in status_counts:
                    status_counts[status] += 1
            except ValueError:
                continue
        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)
except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    sys.exit(0)
      continue
