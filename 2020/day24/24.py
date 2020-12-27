from sys import stdin

l = stdin.read().split("\n")

d = ["se", "sw", "ne", "nw"]

symbol_map = {
    "e": (0, 1),
    "se": (-0.5, 0.5),
    "sw": (-0.5, -0.5),
    "w": (0, -1),
    "nw": (0.5, -0.5),
    "ne": (0.5, 0.5)
}

cleaned = []

for line in l:

    symbols = []

    while len(line) > 0:
        if any(x in line[:2] for x in d):
            symbols.append(line[:2])
            line = line[2:]
        else:
            symbols.append(line[0])
            line = line[1:]

    cleaned.append(symbols)


def art(instructions, days):

    black_tiles = set()

    for line in instructions:

        y = 0
        x = 0

        for direction in line:
            
            dy, dx = symbol_map[direction]
            y += dy
            x += dx

        if (y, x) not in black_tiles:
            black_tiles.add((y, x))
        else:
            black_tiles.remove((y, x))

    cur = black_tiles

    for _ in range(days):

        check = set()

        for y, x in cur:

            check.add((y, x))
            check.update({(y + dy,  x + dx) for dy, dx in symbol_map.values()})

        new_black_tiles = set()

        for y, x in check:

            adjacent = {(y + dy,  x + dx) for dy, dx in symbol_map.values()}
            adjacent_black = len(adjacent & cur)

            if (y, x) in cur and adjacent_black not in [1, 2]:
                continue

            elif (y, x) in cur and adjacent_black in [1, 2]:
                new_black_tiles.add((y, x))

            elif (y, x) not in cur and adjacent_black == 2:
                new_black_tiles.add((y, x))

        cur = new_black_tiles

    return len(cur)

print(art(cleaned, 0))
print(art(cleaned, 100))