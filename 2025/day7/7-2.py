#get input
import os

cwd = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(cwd, "input.txt")

with open(input_path) as f:
    lines = f.read().splitlines()

#solution
from collections import defaultdict

start = lines[0].index("S")

for i in range(len(lines)):
    line = lines[i]

    if "S" in line:
        beams = {start: 1} #dict with beam count instead
        continue

    next_beams = defaultdict(int)
    for beam, count in beams.items():

        if lines[i][beam] == ".": #if empty, transfer timeline count to same row
            next_beams[beam] += count

        elif lines[i][beam] == "^": #if splitter, transfer timeline count to side rows
            next_beams[beam - 1] += count
            next_beams[beam + 1] += count

    beams = next_beams    

total_timelines = sum(beams.values())
print(f"Number of possible timelines: {total_timelines}")