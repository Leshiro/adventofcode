#get input
import os

cwd = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(cwd, "input.txt")

with open(input_path) as f:
    input = f.read().strip()

#solution
input_list = input.split(",")
sum = 0

for range in input_list:
    ends = range.split("-")
    
    start = int(ends[0])
    end = int(ends[1])

    index = start

    while index < end:

        if len(str(index)) % 2 == 0:
            x = int(len(str(index)) / 2)
            
            if str(index)[:x] == str(index)[x:]:
                sum = sum + index
                
        index = index + 1

print(f"The invalid IDs add up to: {sum}")