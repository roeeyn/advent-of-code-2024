with open("./input.txt", "r") as file:
    content = file.read()

reports = [
    [int(num) for num in line.split(" ")] for line in content.split("\n") if line != ""
]

safe_reports = 0

for report in reports:
    is_safe = True
    prev_el = report[0]
    idx = 1
    is_descending = None
    while is_safe and idx < len(report):
        curr_el = report[idx]
        diff = curr_el - prev_el
        abs_diff = abs(diff)
        invalid_diff = diff == 0 or abs_diff > 3
        invalid_desc_sort = diff < 0 and is_descending == False
        invalid_asc_sort = diff > 0 and is_descending == True
        if invalid_diff or invalid_desc_sort or invalid_asc_sort:
            is_safe = False
            continue

        if is_descending is None:
            is_descending = diff < 0

        prev_el = curr_el
        idx += 1

    if is_safe:
        safe_reports += 1


print(safe_reports)
