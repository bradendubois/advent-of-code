from sys import stdin

l = []

for line in stdin:

    l.append(line.rstrip())


def slope(x_slope, y_slope):

    x = 0
    y = 0

    tally = 0

    while y < len(l):
        if l[y][x] == '#':
            tally += 1

        x += x_slope

        x = x % len(l[y])
        y += y_slope

    return tally


# Part 1
print(slope(3, 1))

# Part 2
print(slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2))
