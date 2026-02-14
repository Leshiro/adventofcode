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
    joltage = ""

    print(f"{lineno}) {code}")

    for i in range(12):
        if i == 0:
            start_index = 0

        remaining = 12 - i
        end_index = length-remaining 

        partition = code[start_index:end_index+1]
        print(f"Partition: {start_index}│{partition}│{end_index}")

        largest = 0
        for char in partition:
            if int(char) > largest:
                largest = int(char)
        print(f"Largest: {largest} (index {start_index + partition.index(str(largest))})")

        joltage = joltage + str(largest)
        
        start_index = start_index + partition.index(str(largest)) + 1

    print(f"Max joltage: {joltage}\n")
    lineno = lineno + 1
    total = total + int(joltage)

print(f"The total output joltage should be: {total}")