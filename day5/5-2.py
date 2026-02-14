#get input
import os

cwd = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(cwd, "input.txt")

with open(input_path) as f:
    lines = f.read().splitlines()

#solution
ranges = []
fresh = []

for i in range(len(lines)):
    line = lines[i]

    if line == "":
        index = i
        break

    rangelist = line.split("-")
    ranges.append((int(rangelist[0]), int(rangelist[1])))

#organize ranges
ranges.sort()
organized = []

for a, b in ranges:
    if not organized or a > organized[-1][1] + 1: #if there is a gap, add new range
        organized.append([a, b])
    else:
        organized[-1][1] = max(organized[-1][1], b) #if there is no gap, merge

#count total fresh IDs
fresh_count = sum(b - a + 1 for a, b in organized)

print(f"Number of ingredients that are considered fresh: {fresh_count}")