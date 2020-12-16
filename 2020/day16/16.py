from sys import stdin
import itertools

pre = stdin.read().split("\n\n")

ranges = dict()

class_pre = pre[0].split("\n")

for line in class_pre:
    key, values = line.split(": ")
    ranges[key] = set()
    for r in values.split(" or "):
        
        low, high = [int(x) for x in r.split("-")]
        for i in range(low, high+1):
            ranges[key].add(i)

mine = [int(x) for x in pre[1].split("\n")[1].split(",")]
nearby = [[int(x) for x in ticket.split(",")] for ticket in pre[2].strip().split("\n")[1:]]


good = list()

# Part One
error = 0

for ticket in nearby:

    bad = False

    for value in ticket:
        if not any(value in s for s in ranges.values()):
            error += value
            bad = True

    if not bad:
        good.append(ticket)

print(error)

# Part Two

positions = [""] * len(ranges)
solved = [False] * len(ranges)

remaining = set(ranges.keys())

while True:

    if solved.count(False) == 0:
        break

    for i, solve in enumerate(solved):
        if solve:
            continue

        plausible = [x for x in remaining if all(ticket[i] in ranges[x] for ticket in good)]

        if len(plausible) == 1:

            selected = plausible.pop()
            remaining.remove(selected)
            
            solved[i] = True
            positions[i] = selected


prod = 1
for i, x in enumerate(positions):
    if x.startswith("departure"):
        prod *= mine[i]

print(prod)
