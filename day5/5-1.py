#get input
import os

cwd = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(cwd, "input.txt")

with open(input_path) as f:
    lines = f.read().splitlines()

#solution
ranges = []
ingreds = []

for i in range(len(lines)):
    line = lines[i]

    if line == "":
        index = i
        break

    rangelist = line.split("-")
    ranges.append((int(rangelist[0]), int(rangelist[1])))
    
for id in lines[i+1:]:
    ingreds.append(int(id))

spoiled = []

#get number of spoiled ingredients
for id in ingreds:
    if not any(start <= id <= end for start, end in ranges):
        spoiled.append(id)

print(f"Total ingredients: {len(ingreds)}")
print(f"Spoiled ingredients: {len(spoiled)}")
print(f"Fresh ingredients: {len(ingreds) - len(spoiled)}")