#get input
import os

cwd = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(cwd, "input.txt")

with open(input_path) as f:
    lines = f.read().splitlines()

#solution
total_0 = 0
dial = 50

for line in lines:

    if line[0] == "R":
        direction = 1
    elif line[0] == "L":
        direction = -1
        
    amount = int(line[1:])
    for i in range(amount):
        dial = dial + 1 * direction
        dial = dial % 100

        if dial == 0:
            total_0 = total_0 + 1

print(f"The password must be: {total_0}")