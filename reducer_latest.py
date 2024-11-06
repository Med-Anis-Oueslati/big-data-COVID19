#!/usr/bin/env python3
import sys
from datetime import datetime

# Dictionary to hold the latest date for each key
latest_dates = {}

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue  # Skip empty lines

    fields = line.split(" ")  # Split the input line into fields
    if len(fields) < 2:
        continue

    
    key = fields[0]

    # The date is in the second field
    date_str = " ".join(
        fields[1:]
    )  # Join the remaining fields in case of spaces in the date
    try:
        # Convert the string to a datetime object with the correct format
        current_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError as e:
        continue

    # Update the latest date for the key
    if key not in latest_dates:
        latest_dates[key] = current_date
    else:
        latest_dates[key] = max(latest_dates[key], current_date)


for key, latest_date in latest_dates.items():
    print(f"{key}: Latest Date: {latest_date.strftime('%Y-%m-%d %H:%M:%S')}")
