import itertools
from sys import stdin


def all_tile_points(left_offset, top_offset, width, height):
        
    points = set()

    for w in range(width):
        for h in range(height):            
            points.add((left_offset + w, top_offset + h))

    return points


l = stdin.read().split("\n")

fabric = dict()

cleaned = []

for line in l:
    
    id, at, offset, size = line.split(" ")

    left_offset, top_offset = [int(x) for x in offset.strip(":").split(",")]
    width, height = [int(x) for x in size.split("x")]

    cleaned.append([id, left_offset, top_offset, width, height])

    for point in all_tile_points(left_offset, top_offset, width, height):
        
        if point not in fabric:
            fabric[point] = 0
        fabric[point] += 1


# Part One
print(len([x for x in fabric.values() if x >= 2]))

# Part Two
for line in cleaned:
    
    id = line[0]
    points = all_tile_points(*line[1:])
    
    if all(fabric[point] == 1 for point in points):
        print(id[1:])
        exit()
