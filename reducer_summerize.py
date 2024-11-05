#!/usr/bin/env python3
import sys

# Dictionary to hold maximum values for each state
state_max = {}

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue  # Skip empty lines

    # Split the line by space to separate the state from the counts
    parts = line.split(" (", 1)  # Split into state and the rest
    if len(parts) != 2:
        print(f"Skipping malformed line: {line}", file=sys.stderr)
        continue

    state = parts[0]  # The state name
    counts = parts[1].rstrip(")")  # Get counts, removing trailing ')'

    # Split the counts into individual components
    try:
        confirmed, deaths, recovered = map(float, counts.split(", "))
        confirmed = int(confirmed)
        deaths = int(deaths)
        recovered = float(recovered)  # Keep as float for recovery
    except ValueError:
        print(f"Skipping malformed counts: {counts}", file=sys.stderr)
        continue

    # Update max values by state
    if state not in state_max:
        state_max[state] = {
            "confirmed": confirmed,
            "deaths": deaths,
            "recovered": recovered,
        }
    else:
        # Update the existing state's max values
        state_max[state]["confirmed"] = max(state_max[state]["confirmed"], confirmed)
        state_max[state]["deaths"] = max(state_max[state]["deaths"], deaths)
        state_max[state]["recovered"] = max(state_max[state]["recovered"], recovered)

# Output the maximum values for each state
for state, totals in state_max.items():
    print(
        f"{state}: Max Confirmed: {totals['confirmed']}, Max Deaths: {totals['deaths']}, Max Recovered: {totals['recovered']}"
    )
