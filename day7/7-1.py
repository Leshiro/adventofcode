#get input
import os

cwd = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(cwd, "input.txt")

with open(input_path) as f:
    lines = f.read().splitlines()

#solution
start = lines[0].index("S")
splits = 0

for i in range(len(lines)):
    line = lines[i]

    if "S" in line:
        beams = [start]
        continue

    for beam in beams[:]: #take a beams snapshot
        if lines[i][beam] == ".": #if empty, continue
            lines[i] = lines[i][:beam] + "|" + lines[i][beam+1:]

        elif lines[i][beam] == "^": #if splitter, split
            beams.remove(beam)

            if beam + 1 not in beams:
                beams.append(beam + 1)
            if beam - 1 not in beams:
                beams.append(beam - 1)

            lines[i] = lines[i][:beam-1] + "|" + "^" + "|" + lines[i][beam+2:]
            splits = splits + 1
        
for line in lines:
    print(line)

print(f"Number of splits of the tacyhon beam: {splits}")