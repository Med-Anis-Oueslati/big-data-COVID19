#!/usr/bin/env python3
import sys

max_confirmed = 0  # Initialize max confirmed count
line_max = ""
for line in sys.stdin:
    fields = line.strip().split(" ")  # Split the input line into fields
    confirmed = int(fields[1])

    if confirmed >max_confirmed :
        max_confirmed = confirmed  # Update max confirmed count
        line_max = line.split(" ")  # Split the input line into

print(line_max[0], max_confirmed)
