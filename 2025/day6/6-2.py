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

        line = lines[0]
        i = x
        while i < len(line) and line[i] == " ":
            i = i + 1
        while i < len(line) and not all(s[i] == " " for s in lines):
            i = i + 1

        width = i - x
        numbers = []
        for w in range(width):
            index = x + w
            num = ""
            for lineno in range(len(lines) - 1):
                line = lines[lineno]
                curchar = line[index].strip()
                num = num + curchar
            numbers.append(int(num))
                
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

print(f"The true grand total is: {total}")