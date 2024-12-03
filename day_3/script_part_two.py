import re

file = open("./day_3/input.txt", "r")
content = file.read()
lines = content.split("\n")

result = 0

for line in lines:
    enabled = True
    for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line):
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            l, r = re.findall(r"\d{1,3}", match)
            result += int(l) * int(r)

file.close()

print(result)
