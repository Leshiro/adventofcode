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
vertices = {}
for a in range(len(jboxes)):
    box1 = jboxes[a]
    vertices[a] = box1
    for b in range(a+1, len(jboxes)):
        box2 = jboxes[b]

        distance2 = get_distance(box1, box2)
        distances.append((distance2, a, b))

distances.sort()

def handle_edge(handled_edge):
    distance, v1, v2 = handled_edge
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

circuits = [{i} for i in range(len(jboxes))]

i = 0
while len(circuits) != 1 and i < len(distances): #handle edges until 1 final circuit
    handle_edge(distances[i])
    last_edge = distances[i]
    i += 1

print(f"Final circuit: {circuits[0]}")

distance, v1no, v2no = last_edge
v1, v2 = vertices[v1no], vertices[v2no]
result = v1[0] * v2[0]

print(f"""Last edge: {last_edge}
Last two boxes:
    #{v1no}: {v1}
    #{v2no}: {v2}
Multiplication of their X coordinates: {result}""")