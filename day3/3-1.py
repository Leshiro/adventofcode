#get input
import os

cwd = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(cwd, "input.txt")

with open(input_path) as f:
    lines = f.read().splitlines()

#solution
total = 0
lineno = 1

for code in lines:
    length = len(code)

    largest = 0
    for char in code[:length-1]:
        if int(char) > largest:
            largest = int(char)

    lindex = code.index(str(largest))

    largest2 = 0
    for char in code[lindex+1:]:
        if int(char) > largest2:
            largest2 = int(char)

    joltage = int(str(largest) + str(largest2))
    total = total + joltage

    print(f"{lineno}) {code}")
    print(f"Largest 1: {largest} (index: {lindex})")
    print(f"Largest 2: {largest2} (index: {code.index(str(largest2))})")
    print(f"Max joltage: {joltage}\n")
    lineno = lineno + 1

print(f"The total output joltage should be: {total}")