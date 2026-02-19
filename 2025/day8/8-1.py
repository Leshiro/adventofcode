#get input
import os

cwd = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(cwd, "input.txt")

with open(input_path) as f:
    lines = f.read().splitlines()

#solution
jboxes = []

for line in lines:
    jbox = line.split(",")
    x = int(jbox[0])
    y = int(jbox[1])
    z = int(jbox[2])
    jbox = (x, y, z)
    jboxes.append(jbox)

def get_distance(box1, box2):
    x1, y1, z1 = box1
    x2, y2, z2 = box2
    distance2 = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2 #no need for sqrt
    return distance2

distances = []
for a in range(len(jboxes)):
    box1 = jboxes[a]
    for b in range(a+1, len(jboxes)):
        box2 = jboxes[b]

        distance2 = get_distance(box1, box2)
        distances.append((distance2, a, b))

distances.sort()

circuits = [{i} for i in range(len(jboxes))]

for i in range(1000):
    distance, v1, v2 = distances[i]
    current_vertices = {v1, v2}
    
    if circuits == []: #if empty, create circuit with vertices in current edge
        circuits.append(current_vertices)

    else:
        matches = []
        for cno in range(len(circuits)):
            circuit = circuits[cno]
            
            if v1 in circuit or v2 in circuit:
                matches.append(cno)

        if len(matches) == 0: #if no match, create new circuit with vertices in current edge
            circuits.append(current_vertices)
            
        elif len(matches) == 1: #if only 1 match, add to it
            circuits[matches[0]].update(current_vertices)

        elif len(matches) >= 2: #if multiple matches, merge, then add to it
            main = min(matches) #define main circuit

            for match in matches: #merge circuits
                if match != main:
                    circuits[main].update(circuits[match])
            circuits[main].update(current_vertices) #add vertices in current edge

            matches = sorted(set(matches))
            for match in matches[::-1]: #delete already merged circuits
                if match != main:
                    del circuits[match]

top3 = []
result = 1
while len(top3) < 3:
    largest = 0
    for k in range(len(circuits)):
        circ = circuits[k]
        if len(circ) > largest:
            largest = len(circ)
            index = k
    del circuits[index]
    top3.append(largest)
    result = result * largest

print(f"The sizes of the 3 largest circuits: {top3}\nMultiplication: {result}")