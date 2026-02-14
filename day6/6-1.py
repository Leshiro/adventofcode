#get input
import os

cwd = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(cwd, "input.txt")

with open(input_path) as f:
    lines = f.read().splitlines()

#solution
operations = lines[4]

total = 0

for x in range(len(operations)):
    char = operations[x]
    if char != " ":

        numbers = []
        for y in range(len(lines) - 1):
            line = lines[y]
            num = ""
            i = x
            if line[i] == " ":
                while i < len(line) and line[i] == " ":
                    i = i + 1
            while i < len(line) and line[i] != " ":
                num = num + line[i]
                i = i + 1
            if num.strip() != "":
                num = int(num)
                numbers.append(num)

        if char == "+":
            result = 0
        elif char == "*":
            result = 1
            
        for num in numbers:
            if char == "+":
                result = result + num
            elif char == "*":
                result = result * num 
        total = total + result

print(f"The grand total is: {total}")