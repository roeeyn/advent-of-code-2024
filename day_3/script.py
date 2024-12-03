import re

file = open("./day_3/input.txt", "r")
content = file.read()
lines = content.split("\n")

result = 0

for line in lines:
    match_list = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
    result += sum([int(l) * int(r) for l, r in match_list])
