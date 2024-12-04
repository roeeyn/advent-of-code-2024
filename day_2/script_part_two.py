def is_safe(report):
    # Determine direction
    direction = None
    for i in range(len(report) - 1):
        if report[i] < report[i + 1]:
            direction = "inc"
            break
        elif report[i] > report[i + 1]:
            direction = "dec"
            break

    if direction is None:
        # No differing elements; all are equal or single element
        # Equal elements mean no valid "increasing" or "decreasing" trend
        return False

    # Check differences based on direction
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if direction == "inc":
            if diff < 1 or diff > 3:
                return False
        else:
            # direction == 'dec'
            if diff > -1 or diff < -3:
                return False
    return True


def is_safe_with_dampener(report):
    # If already safe
    if is_safe(report):
        return True

    # Try removing one element at a time
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1 :]
        if is_safe(new_report):
            return True

    # If no single removal leads to a safe report
    return False


# Process input
with open("day_2/input.txt", "r") as f:
    data = [list(map(int, line.split())) for line in f if line.strip()]

count = 0
for report in data:
    if is_safe(report) or is_safe_with_dampener(report):
        count += 1

print(count)
