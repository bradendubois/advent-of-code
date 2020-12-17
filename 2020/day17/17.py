from sys import stdin

import itertools
import operator

l = stdin.read().split("\n")

offsets = (-1, 0, 1)

def solve(initial2D, dimensions):

    data = set()
    for y, r in enumerate(l):
        for x, c in enumerate(r):
            if c == "#":
                data.add((y, x, *[0]*(dimensions-2)))

    def cycle(on_points):

        dimensional_offsets = {x for x in itertools.product(*[offsets]*dimensions)}
        evaluate = set()

        for p in on_points:
            for o in dimensional_offsets:
                evaluate.add(tuple(map(operator.add, p, o)))

        next_state = set()

        for e in evaluate:

            adjacent_on = 0

            for o in dimensional_offsets:
                adj = tuple(map(operator.add, e, o))

                if adj != e and adj in on_points:
                    adjacent_on += 1

            if e in on_points and adjacent_on in (2, 3):
                next_state.add(e)

            elif e not in on_points and adjacent_on == 3:
                next_state.add(e)

        return next_state

    for _ in range(6):
        data = cycle(data)

    return len(data)

# Part One
print(solve(l, 3))

# Part Two
print(solve(l, 4))
