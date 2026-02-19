#get input
import os

cwd = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(cwd, "input.txt")

with open(input_path) as f:
    lines = f.read().splitlines()

#solution
len_x = len(lines[0])
len_y = len(lines)

adjacent = [-1, 0, 1]

accesible = 0

for y in range(len(lines)):
    line = lines[y]
    for x in range(len(line)):
        char = line[x]

        if char != "@":
            continue

        ap = 0
        for change_x in adjacent:
            for change_y in adjacent:

                if (change_x, change_y) == (0, 0):
                    continue
                
                else:
                    if len_x - 1 >= x + change_x >= 0 and len_y - 1 >= y + change_y >= 0:
                        checked_char = lines[y + change_y][x + change_x]
                        if checked_char == "@":
                            ap = ap + 1
        if ap < 4:
            accesible = accesible + 1
        
print(f"The number of paper rolls accessible by a forklift: {accesible}")