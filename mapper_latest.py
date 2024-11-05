#!/usr/bin/env python3
import sys
import csv

# Use csv.reader directly since Get-Content gives us a list of lines
reader = csv.reader(sys.stdin, delimiter=",")  # Adjust the delimiter if necessary
next(reader)  # Skip header if present

for fields in reader:
  state = fields[0]  # Province_State
  last_update = fields[2]  # Last_Update
  print(state, last_update)