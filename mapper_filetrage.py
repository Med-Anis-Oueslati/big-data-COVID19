#!/usr/bin/env python3
import sys
import csv

# Use csv.reader directly since Get-Content gives us a list of lines
reader = csv.reader(sys.stdin, delimiter=",")  # Adjust the delimiter if necessary
next(reader)  # Skip header if present

for fields in reader:
    confirmed = int(fields[5])  # Assuming this is the index for the confirmed count
    if confirmed > 10000000:
        print(fields[0], fields[5])  # Emit the entire line for further processing
