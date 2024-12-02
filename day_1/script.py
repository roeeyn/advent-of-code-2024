# PART 1
with open("./sorted_input_1.txt", "r") as file:
    content_left = file.read()

with open("./sorted_input_2.txt", "r") as file:
    content_right = file.read()

left = [int(line) for line in content_left.split("\n") if line != ""]

right = [int(line) for line in content_right.split("\n") if line != ""]

sum = 0
for i in range(1000):
    sum += abs(right[i] - left[i])

sum

# PART 2
right_map = {}
for el in right:
    right_map[el] = right_map.get(el, 0) + 1

right_map

left_score = [el * right_map.get(el, 0) for el in left]

left_score

sum = 0
for i in left_score:
    sum += i

sum
