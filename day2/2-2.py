#get input
import os

cwd = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(cwd, "input.txt")

with open(input_path) as f:
    input = f.read().strip()

#solution
input_list = input.split(",")
sum = 0

for ranges in input_list:
    ends = ranges.split("-")
    start = int(ends[0])
    end = int(ends[1])

    index = start

    while index < end:
        s = str(index)

        if len(s) >= 2 and s in (s + s)[1:-1]:
            sum = sum + index

        index = index + 1

print(f"The invalid IDs add up to: {sum}")