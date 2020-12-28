import itertools
from sys import stdin

l = stdin.read().split("\n")


candidates_two = set()
candidates_three = set()

for line in l:
    if any(line.count(x) == 2 for x in set(line)):
        candidates_two.add(line)
    
    if any(line.count(x) == 3 for x in set(line)):
        candidates_three.add(line)


# Part One
print(len(candidates_two) * len(candidates_three))


# Part Two
for box_1, box_2 in itertools.product(l, l):
    
    comparison = [box_1[i] for i in range(len(box_1)) if box_1[i] == box_2[i]]

    if len(comparison) == len(box_1) - 1:
        print("".join(comparison))
        exit()
